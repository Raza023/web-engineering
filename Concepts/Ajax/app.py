from flask import Flask,render_template,request,session,jsonify
from AddressBookModel import AddressbookModel
from ViewClasses import *

app = Flask(__name__)
app.config.from_object("config")
app.secret_key=app.config["SECRET_KEY"]

@app.route('/')
def hello_world():
    return render_template("Login.html",error=False,errormsg=None)

@app.route("/signupform")
def signupform():
    return render_template("Signup.html", error=False, errormsg=None)

@app.route("/signup", methods=["POST"])
def signup():
    email = request.form["email"]
    password = request.form["pwd"]
    user=User(email,password)
    model=AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    exist=model.checkUserExist(user)
    if not exist:
        insert=model.insertUser(user)
        if insert:
            return render_template("Test.html",name=email)
        else:
            return render_template("Signup.html", error=True , errormsg="Some error in signup")
    else:
        return render_template("Signup.html",error=True,errormsg="Email already exist")

@app.route("/login", methods=["POST"])
def login():
    email=request.form["email"]
    pwd=request.form["pwd"]
    user=User(email,pwd)
    model=AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    if model.loginUser(user):
        session["email"] = email
        session["pwd"] = pwd
        # response = make_response(render_template("Dashboard.html" , log= "You are logged in.", email=email))
        # response.set_cookie("email", email)
        # response.set_cookie("pwd", pwd)
        # return response
        return render_template("Dashboard.html" , log= "You are logged in.", email=email)
    else:
        return render_template("Login.html", error=True,errormsg="username or password invalid")

@app.route("/dashboard")
def dashboard():
    #email=request.cookies.get("email")
    email = session.get("email")
    if email != None:
        return render_template("Dashboard.html" , email=email)
    else:
        return render_template("Login.html", error=True, errormsg="Please log in first.")

@app.route("/addcontact")
def addContact():
    #email = request.cookies.get("email")
    email = session.get("email")
    if email != None:
        return render_template("createContact.html",email=email, error=False, errormsg=None)
    else:
        return render_template("Login.html", error=True, errormsg="Please log in first.")

@app.route("/createcontact", methods=["POST"])
def cretaecontact():
    #email = request.cookies.get("email")
    email = session.get("email")
    if email != None:
        name = request.form["name"]
        mobile = request.form["mobile"]
        city = request.form["city"]
        profession = request.form["profession"]
        contact = Contact(name, mobile, city, profession)
        model = AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        add = model.insertContact(contact)
        if add:
            return render_template("createContact.html", add="Contact added", error=False, errormsg=None,email=email)
        else:
            return render_template("createContact.html", error=True, errormsg="Some error in creating contact.",email=email)
    else:
        return render_template("Login.html",error=True,errormsg="Please log in first.")


@app.route("/deletecontact", methods=["POST"])
def deletecontact():
    #email = request.cookies.get("email")
    email = session.get("email")
    if email != None:
        model = AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        deleted = model.deleteContact()
        if deleted:
            return render_template("deleting.html", add="Contact deleted", error=False, errormsg=None,email=email)
        else:
            return render_template("deleting.html", error=True, errormsg="Some error in deleting contact.",email=email)
    else:
        return render_template("Login.html", error=True, errormsg="Please log in first.")

@app.route("/getcontact")
def getContact():
    #email = request.cookies.get("email")
    email = session.get("email")
    if email != None:
        model = AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        list1 = model.getContact()
        return render_template("updatecontact.html", error=False, errormsg=None, email=email, list1 = list1)
    else:
        return render_template("Login.html", error=True, errormsg="Please log in first.")

@app.route("/updatecontact", methods=["POST"])
def updatecontact():
    #email = request.cookies.get("email")
    email = session.get("email")
    if email != None:
        model = AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        cn = request.form["name"]
        cid=model.getOneContact(cn)
        c_id.append(cid)
        list1 = model.getContact()
        if cid == None:
            return render_template("updatecontact.html", error=True, errormsg="No contact found", email=email,list1=list1)
        else:
            return render_template("getcontact.html", error=False, errormsg=None, email=email)
        # response1.set_cookie("cid",c_id)
        # response1.set_cookie("cname", cn)
        # return response1
    else:
        return render_template("Login.html", error=True, errormsg="Please log in first.")

@app.route("/getContacts" , methods=["GET"])
def getDonors():
    model = AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    city = request.args.get("val")
    contactList=model.getCityContacts(city)
    return jsonify(contactList)

@app.route("/update", methods=["POST"])
def update():
    #email = request.cookies.get("email")
    email = session.get("email")
    if email != None:
        model = AddressbookModel(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
        # cn = request.cookies.get("cname")
        # cid = request.cookies.get("cid")
        cid = c_id.pop()
        c_id.append(cid)
        print(cid)
        name=request.form["name"]
        print(name)
        mobile=request.form["mobile"]
        print(mobile)
        city=request.form["city"]
        print(city)
        profession=request.form["profession"]
        print(profession)
        cont = Contact(name,mobile,city,profession)
        update = model.updateContact(cont , cid)
        if update:
            return render_template("showupdatestatus.html", error=False, errormsg=None, email=email, msg="Contact has been updated")
        else:
            return render_template("getcontact.html", error=True, errormsg="Error in updating contact", email=email)
    else:
        return render_template("Login.html", error=True, errormsg="Please log in first.")

@app.route("/showuser")
def showUser():
    #email = request.cookies.get("email")
    email = session.get("email")
    #pwd = request.cookies.get("pwd")
    pwd = session.get("pwd")
    return render_template("ShowUser.html",email=email,pwd=pwd)

@app.route("/logout")
def logout():
    # response = make_response(render_template("Login.html"))
    # response.delete_cookie("pwd")
    # response.delete_cookie("email")
    # return response
    session.clear()
    return render_template("Login.html")

if __name__ == '__main__':
    app.run(debug=True)

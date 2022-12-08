from flask import Flask,render_template,request,session,jsonify
from model import model
from view import *

app = Flask(__name__)

app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]

Model=model(app.config["HOST"],app.config["USER"],app.config["PASSWORD"],app.config["DATABASE"])

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
    exist= Model.checkUserExist(user)
    if not exist:
        insert=Model.insertUser(user)
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
    if Model.loginUser(user):
        session['email'] = email
        session['pwd'] = pwd
        return render_template("Dashboard.html" , log= "You are logged in.", email=email)
    else:
        return render_template("Login.html", error=True,errormsg="username or password invalid")

@app.route("/dashboard")
def dashboard():
    email = session.get("email")
    # email=request.cookies.get("email")
    if email!=None:
        return render_template("Dashboard.html" , email=email)
    else:
        return render_template("Login.html", error=True,errormsg="You must have to login first.")
   

@app.route("/addcontact")
def addContact():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email!=None:
        return render_template("createContact.html",email=email, error=False, errormsg=None)
    else:
        return render_template("Login.html", error=True,errormsg="You must have to login first.")

@app.route("/createcontact", methods=["POST"])
def cretaecontact():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email != None:
        name = request.form["name"]
        mobile = request.form["mobile"]
        city = request.form["city"]
        profession = request.form["profession"]
        contact = Contact(name, mobile, city, profession)
        add = Model.insertContact(contact)
        if add:
            return render_template("createContact.html", add="Contact added", error=False, errormsg=None,email=email)
        else:
            return render_template("createContact.html", error=True, errormsg="Some error in creating contact.",email=email)
    else:
        return render_template("login.html",error=True,errormsg="Please log in first.")


@app.route("/deletecontact", methods=["POST"])
def deletecontact():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email != None:
        deleted = Model.deleteContact()
        if deleted:
            return render_template("deleting.html", add="Contact deleted", error=False, errormsg=None,email=email)
        else:
            return render_template("deleting.html", error=True, errormsg="Some error in deleting contact.",email=email)
    else:
        return render_template("login.html", error=True, errormsg="Please log in first.")

@app.route("/getcontact")
def updateContact():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email != None:
        update = Model.getContact()
        return render_template("updatecontact.html", error=False, errormsg=None, email=email, list1 = update)
    else:
        return render_template("login.html", error=True, errormsg="Please log in first.")

@app.route("/getcontacts",methods=["GET"])
def getcontacts():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email != None:
        city = request.args.get("city")
        update = Model.getCityContact(city)
        return jsonify(update)
    else:
        return render_template("login.html", error=True, errormsg="Please log in first.")

@app.route("/updatecontact", methods=["POST"])
def updatecontact():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email != None:
        cn = request.form["name"]
        cid=Model.getOneContact(cn)
        c_id.append(cid)
        list1 = Model.getContact()
        if cid == None:
            return render_template("updatecontact.html", error=True, errormsg="No contact found", email=email,list1=list1)
        else:
            return render_template("getcontact.html", error=False, errormsg=None, email=email)
        # response1.set_cookie("cid",c_id)
        # response1.set_cookie("cname", cn)
        # return response1
    else:
        return render_template("login.html", error=True, errormsg="Please log in first.")


@app.route("/update", methods=["POST"])
def update():
    email = session.get("email")
    # email = request.cookies.get("email")
    if email != None:
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
        update = Model.updateContact(cont , cid)
        if update:
            return render_template("showupdatestatus.html", error=False, errormsg=None, email=email, msg="Contact has been updated")
        else:
            return render_template("getcontact.html", error=True, errormsg="Error in updating contact", email=email)
    else:
        return render_template("login.html", error=True, errormsg="Please log in first.")

@app.route("/showuser")
def showUser():
    email = session.get("email")
    # email = request.cookies.get("email")
    pwd = session.get("pwd")
    # pwd = request.cookies.get("pwd")
    return render_template("ShowUser.html",email=email,pwd=pwd)

@app.route("/logout")
def logout():
    session.clear()
    return render_template("Login.html")

if __name__ == '__main__':
    app.run()
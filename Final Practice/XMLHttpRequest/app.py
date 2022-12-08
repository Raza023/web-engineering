from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ghost123"

text = []
@app.route('/')
def home():
    if session.get('username') == None:
        return render_template("login.html")
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['name']
    session['username'] = username
    return render_template('home.html')

@app.route('/message', methods=['post'])
def message():
    global text
    text.append(f"<i><b>[{session['username']}]: </b></i>" + request.form['text'])
    return "recieved"

@app.route('/getMessages')
def getMessages():
    global text
    if len(text) > 0:
        temp = ''
        for i in text:
            temp = temp + i +'<br>'
        return temp
    else:
        return "none"

@app.route('/del')
def annoRoute():
    global text
    text = list()
    return redirect('/')

@app.route('/clear')
def annoRoute2():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
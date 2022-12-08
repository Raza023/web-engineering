from model import EarthJoyModel
from flask import Flask,render_template,request,session,redirect,url_for,session
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)

app = Flask(__name__)
socketio = SocketIO(app)
app.config.from_object("config")
app.secret_key=app.config["SECRET_KEY"]
def getModel():
    return EarthJoyModel(app.config["HOST"],app.config["USER"],app.config["PASSWORD"], app.config["DATABASE"])


MODEL = getModel()


@app.route('/')
def login():
    return render_template('chatHome.html')


@app.route('/buyerLoginForm')
def buyerLoginForm():
    return render_template('buyerLogin.html')


@app.route('/sellerLoginForm')
def sellerLoginForm():
    return render_template('sellerLogin.html')


@app.route('/buyerLogin',methods=["post"])
def buyerLogin():
    username = request.form["username"]
    password = request.form["password"]
    session["ID"]  = MODEL.getBuyerID(username)
    session["username"] = username
    return render_template('buyerEnd.html',sellers=MODEL.getSellerIDs()) if MODEL.buyerLogin(username,password) else render_template('buyerLogin.html')



@app.route('/sellerLogin',methods=["post"])
def sellerLogin():
    username = request.form["username"]
    password = request.form["password"]
    session["ID"]  = MODEL.getSellerID(username)
    session["username"] = username
    print(username)
    print(session["ID"])
    return render_template('sellerEnd.html',buyers=MODEL.getBuyerIDs()) if MODEL.sellerLogin(username,password) else render_template('sellerLogin.html')
    


@app.route('/buyer/<int:buyerID>')
def buyer(buyerID):
    MODEL.getMessages(f"{buyerID}{session['ID']}")
    return render_template('chatApp.html',roomID=f"{buyerID},{session['ID']}",username=session["username"],messages=MODEL.getMessages(f"{buyerID},{session['ID']}"))


@app.route('/seller/<int:sellerID>')
def seller(sellerID):
    return render_template('chatApp.html',roomID=f"{session['ID']},{sellerID}",username=session["username"],messages=MODEL.getMessages(f"{session['ID']},{sellerID}"))

@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message'],data['time']))
    
    MODEL.addMessage( data['room'], data['message'], data['time'] ,data['username'])
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])


if __name__=="__main__":
    socketio.run(app,debug=True)
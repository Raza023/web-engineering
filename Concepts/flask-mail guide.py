https://youtu.be/48Eb8JuFuUI

pip install flask-mail

----------------------------app.py-----------------------------------
from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['DEBUG'] = True            
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'            # ('localhost')
app.config['MAIL_PORT'] = 465                            #(default 25 or 465 or 587) 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True                            default app.debug
app.config['MAIL_USERNAME'] = 'imhraza023@gmail.com'
app.config['MAIL_PASSWORD'] = 'qxwsafbsctqznzix'
app.config['MAIL_DEFAULT_SENDER'] = ('Earth Joy','imhraza023@gmail.com')    #  (None)
app.config['MAIL_MAX_EMAILS'] = None                            #(5)
#app.config['MAIL_SUPPRESS_SEND'] = False                     # default app.testing
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello from the other side!', recipients = ['hr770735@gmail.com'])
    msg.html = "<h2>Hey Paul, sending you this email from my Flask app, lmk if it works</h2>"
    mail.send(msg)
    return "Message has been sent!"

if __name__ == '__main__':
   app.run(debug = True)
   

---------------------------------------setting up-----------------------------------------
1 The server is "smtp.gmail.com".
2 The port must match the type of security used.
   >If using STARTTLS with MAIL_USE_TLS = True, then use MAIL_PORT = 587.
   >If using SSL/TLS directly with MAIL_USE_SSL = True, then use MAIL_PORT = 465.
   >Enable either STARTTLS or SSL/TLS, not both.
3 Depending on your Google account's security settings, you may need to generate and use an app password(https://security.google.com/settings/security/apppasswords) rather than the account password. This may also require enabling 2-step verification. You should probably set this up anyway.
4 You must have '2-step verification' enabled on your Google account before you're able to set up app-specific passwords.

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'username@gmail.com'
MAIL_PASSWORD = 'app password generated in step 3'


-----------------------------------------Tutorial---------------------------------
@app.route("/")
def index():
    msg = Message('Hello from the other side!', recipients = ['hr770735@gmail.com'])
    #msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
     msg.html = "<h2>Hey Paul, sending you this email from my Flask app, lmk if it works</h2>"
    mail.send(msg)
    return "Message sent!"

--------------------------------------Customizing a bit----------------------------------------------
msg = Message('Hello from the other side!', sender =  ("Peter from Mailtrap", 'peter@mailtrap.io') , recipients = ['hr770735@gmail.com'])

msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
msg.html = "<b>Hey Paul</b>, sending you this email from my <a href="https://google.com">Flask app</a>, lmk if it works"

flask-mail.Message(subject, recipients, body, html, sender, cc, bcc, reply-to, date, charset, extra_headers, mail_options, rcpt_options)
msg = Message(
    subject = "",
    recipients = [],
    body = "",
    html = "",
    sender = "",
    cc = [],
    bcc = [],
    reply-to = [],
    date = 'date',
    charset = "",
    extra_headers = {'':''},
    mail_options = [],
    rcpt_options = []
)

-------------------------------------------Adding an attachment-----------------------------------------------------
with app.open_resource("invoice.pdf") as fp:  
    msg.attach("invoice.pdf", "application/pdf", fp.read())
#application/pdf is minetype

@app.route("/")
def index():
    msg = Message('Earth Joy', recipients = ['hr770735@gmail.com'])
    #msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    msg.html = "<h2>Hey Paul, sending you this email from my Flask app, lmk if it works</h2>"
    with app.open_resource("cat.jpg") as fp:  
        msg.attach("cat.jpg", "image/jpeg", fp.read())
    mail.send(msg)
    return "Message sent!"

-------------------------------------------Sending bulk messages---------------------------------------------------
with mail.connect() as conn:
    for user in users:
        message = '...'
        subject = "Hello from the other side!"
        msg = Message(
            recipients=[user.email],
            body=message,
            subject=subject
        )
        conn.send(msg)

@app.route('/bulk')
def bulk():
    users = [{"name":"Hassan","email":"hr770735@gmail.com"},{"name":"Ali","email":"hr7760735@gmail.com"}]
    with mail.connect() as conn:
    for user in users:
        message = 'Congratulations! Your account has been verified'
        subject = "Account verification"
        msg = Message(
            recipients=[user["email"]],
            body=message,
            subject=subject
        )
        conn.send(msg)
        
        
SMTP:
https://youtu.be/1Xvb2n17FqU
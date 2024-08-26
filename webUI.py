from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
from lovetester import test_love

app = Flask(__name__)

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
    #display the "results"
    return render_template("results.html", you=your_name, crush=crush_name, score=love_score, message=msg)

#run the flask app
if __name__ == '__main__':
    app.run(debug=True)

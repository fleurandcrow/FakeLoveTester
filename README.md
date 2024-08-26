# FakeLoveTester
A prototype for a "Love Tester" website that emails the user's name and crush name inputs to a specified email

Please keep in mind that this code does not work out of the box and requires manual configuration.

## Things to configure

Before being able to run the script, email credentials will have to configured in the code. This includes a sender email that will send emails via the code and a receiver email that receives the sent emails.

First of all, the SMTP email credentials (lines 8-13) must be set correctly:

```python
#these mail settings have to be changed in order for the mail sending to work
app.config['MAIL_SERVER']= 'smtp.server.here' #replace with your actual SMTP server
app.config['MAIL_PORT'] = 465 #mail port varies depending on the service
app.config['MAIL_USERNAME'] = 'your@email.here' #replace with your actual email
app.config['MAIL_PASSWORD'] = 'your_password_here' #replace with your actual email password
app.config['MAIL_USE_TLS'] = True
```
The recipient email address(es) must also be configured, any valid email address or alias may be used as a recipient.

```python
    #sends you (or any recipient) the name of the user and the name of their crush
    message = Message(
            subject=f"{your_name} has a crush...",
            recipients=['receiver@email.here'], #the recipients can be set to any valid email address(es)
            sender='your@email.here', #the sender must be your SMTP email
            ) 
    message.body = f"{your_name} has a crush on {crush_name}!"
```
The code does not provide any SMTP sender email address, thus you will need to obtain and use your own SMTP email. 

## Usage

This script will have to be run in a terminal, it can be ran on Windows, Mac or Linux. 

First, change your directory to where you have cloned the repository.

Then, run the webUI.py script

```bash
python3 webUI.py
```

or 

```bash
python webUI.py
```


Next, navigate to `http://127.0.0.1:5000/` in your web browser (any web browser will do, chromium and firefox have been tested)
There, you should see the webUI pop up

## Making a fork

This project is a prototype and it may be forked to be used as a base for another project.

## Support

If there are any bugs in the code, feel free to write an issue!

## Authors and acknowledgement

All code in this project was written by me. However, the background image on the webUI was taken from a stock image website.

Credits:

-All images used were from royalty free sources-

Heart image in the CSS has been sourced from: [pexels](https://www.pexels.com/photo/heart-pattern-on-pink-background-7679705/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    
    reply_msg = request.form.get('Body').lower()
    responded = False
    resp = MessagingResponse()
    msg = resp.message()

    if "taxi" in reply_msg:
       reply_msg("Welcome to whatsapp taxi booking.\n1.Book a taxi\n2.About us")

       if reply_msg == 1:
            reply_msg("Enter city")
            if reply_msg == "harare"  :
               reply_msg("Taxi has been booked.\nNow share your location using your whatsapp")
            else:
                reply_msg("Sorry they are no available taxis in your city")
       else:
            reply_msg("hhhhhhhhhhhhhh")
   
    else:
        reply_msg("For booking a taxi type the word\n-Taxi")


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)








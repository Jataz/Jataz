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
    # resp.message("You Said: {}".format(reply_msg))

    # if "taxi" in reply_msg:
    #    msg.body("Welcome to whatsapp taxi booking.\n1.Book a taxi\n2.About us")

    #    if reply_msg == 1:
    #         msg.body("Enter city")
    #         if reply_msg == "harare"  :
    #            msg.body("Taxi has been booked.\nNow share your location using your whatsapp")
    #         else:
    #             msg.body("Sorry they are no available taxis in your city")
    #    else:
    #         msg.body("hhhhhhhhhhhhhh")
   
    # else:
    #     msg.body("For booking a taxi type the word\n-Taxi")

    if 'taxi' in reply_msg:
        msg.body("Book Taxi? Reply *book*")
        
    elif 'book' in reply_msg:
        msg.body('Enter City')
                
    elif 'harare' in reply_msg:
        msg.body('Taxi has been booked')
                
    else:
        msg.body('Sorry they are no available taxis in your city')




    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

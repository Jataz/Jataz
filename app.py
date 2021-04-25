from flask import Flask, request, session, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import requests
import random, os
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "this-is-a-secret-key"

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming messages """
    
    msg = request.form.get('Body').lower()
    number = request.form.get('From').replace("whatsapp:", " ")
    date = datetime.today()
    resp = MessagingResponse()
        
    
   
    if "taxi" in msg:
        connection = sqlite3.connect('WhatsappTaxiOrg.db')
        connection.execute("INSERT INTO customers (phone_number, date_and_time) VALUES (?, ?)", (number, date ))
        connection.commit()
        connection.close()
        session["stage"] = "stage2" 
        resp.message("🚕🚖🇿🇼🚕🚖\n*Welcome to whatsapp taxi booking. Type in your option:*\n\n1.Book a taxi\n2.About Us\n🚕🚖🇿🇼🚕🚖\n\n")
        resp.message(number)

    elif "stage" in session:
        stage = session["stage"] 
        if stage == "stage2" and msg =="1":
            session["stage"] = "booking"
            resp.message("*🏙️🌆Enter your current city*")

        elif stage == "stage2" and msg =="2":
            session["stage"] = "stage2"
            resp.message("*🇿🇼🚖ABOUT US🚖🇿🇼*\n\nXXXXXXXXXXXXX")


        elif stage == "booking" and msg =="harare":
            session["stage"] = "stage3"
            resp.message("*Share your live location*📍")


        elif stage == "booking" and msg != "harare":
            session["stage"] = "stage3"
            resp.message(f"*😕🙇🏽Sorry, currently they are no taxis available in {msg}.*\nType the word *Taxi* to go back to menu.")


        elif stage == "stage3":
            if 'Latitude' in request.values.keys() and 'Longitude' in request.values.keys():
                session["stage"] = "user_location" 
        
                message_latitude = request.values.get('Latitude', None),
                message_longitude = request.values.get('Longitude', None),
                message_address = request.values.get('Address', None)

    
            #resp.message("Your latitude is :" +str(message_latitude) +"\nYour Longitude is :"+ str(message_longitude)+" \n Your address is :" + str(message_address))
                PersistentAction= f'geo:Your Latitude is {message_latitude}\nYour Longitude is {message_longitude}\n{message_address}'
                resp.message(PersistentAction)
                

            elif 'Latitude' not in request.values.keys() and 'Longitude' not in request.values.keys():
                session["stage"] = "user_location" 
                resp.message("❌Invalid location❌\nType the word *Taxi* to go back to menu")


        elif stage == "stage2" and msg != "1" or "2":
            session["stage"] = "stage2"
            resp.message("❌Invalid input❌\nType the word *Taxi* to get started.")

    else:
        resp.message("❌Invalid input❌\nType the word *Taxi* to get started.")

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)








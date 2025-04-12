from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    response = MessagingResponse()
    msg = response.message()

    if "habari" in incoming_msg.lower():
        msg.body("Nzuri sana! Na wewe je?")
    elif "jina lako" in incoming_msg.lower():
        msg.body("Mimi ni bot wa WhatsApp kutoka Render!")
    else:
        msg.body(f"Hujambo! Umesema: {incoming_msg}")

    return str(response)

@app.route("/")
def home():
    return "WhatsApp Bot is Running!"

if __name__ == "__main__":
    app.run()
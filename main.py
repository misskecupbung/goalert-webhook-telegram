# Simple Flask server for redirecting messages from GoAlert 
import requests
import re
from flask import Flask, request
from config import Config

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    
    # Health check endpoint.
    

    return "Healthy"


@app.route("/telegram/<username>", methods=["POST"])
def tg_pm(username):
    
    # Telegram endpoint for webhooks resend.
    
    token = Config.TELEGRAM_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage?parse_mode=Markdown'

    # data of post payload
    data = request.json
    # Get GoAlert type from post payload
    if data["Type"] == "Verification":
        tg_data = "GoAlert Verification code is {0}".format(data["Code"])
    elif data["Type"] == "Alert":
        details = re.sub("## Payload.*", "",
                         str(data["Details"]), flags=re.DOTALL)
        tg_data = "[GoAlert-{1}]({0}/alerts/{1}) {2} {3}".format(
            Config.GOALERT_URL, str(data["AlertID"]), data["Summary"], details
        )
    elif data["Type"] == "AlertStatus":
        tg_data = "[GoAlert-{1}]({0}/alerts/{1}) update status {2}".format(
            Config.GOALERT_URL, str(data["AlertID"]), data["LogEntry"]
        )
    elif data["Type"] == "Test":
        tg_data = "This is a [GoAlert]({0}) test message".format(
            Config.GOALERT_URL)

    data = {'chat_id': username, 'text': tg_data}
    private_message = requests.post(url, data).json()

    return private_message


if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)

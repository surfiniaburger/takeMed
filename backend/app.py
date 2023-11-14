import os
from flask import Flask, request, jsonify
from twilio.rest import Client


# Initialize Flask app
app = Flask(__name__)


# Twilio credentials
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_ACCOUNT_TOKEN')

client = Client(account_sid, auth_token)

# API endpoint to send medication reminders
@app.route('/send-reminder', methods=['POST'])
def send_reminder():
    try:
        data = request.get_json()
        user_phone_number = data.get('phone_number')
        medication_name = data.get('medication_name')

        message_body = f"Don't forget to take your {medication_name} medication today!"

        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=+14088374661,
            to=user_phone_number
        )

        return jsonify({'message_sid': message.sid}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
import redis
import json


# Initialize Flask app
app = Flask(__name__)

# Initialize Redis connection
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_port = os.environ.get('REDIS_PORT', 6379)
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


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
        
        # Check if the data is in the cache
        cache_key = f"{user_phone_number}:{medication_name}"
        cached_data = redis_client.get(cache_key)

        if cached_data:
            return jsonify({'message': 'Reminder already sent for this medication'}), 200

        message_body = f"Don't forget to take your {medication_name} medication today!"

        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=+14088374661,
            to=user_phone_number
        )
        
        # Cache the data to prevent duplicate reminders
        redis_client.setex(cache_key, 3600, json.dumps({'reminder_sent': True}))
        return jsonify({'message_sid': message.sid}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
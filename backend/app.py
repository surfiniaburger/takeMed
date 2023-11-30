import os
from flask import Flask, request, jsonify
from twilio.rest import Client
import redis
import json
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()


# Initialize Flask app
app = Flask(__name__)

# Initialize MongoDB connection with the connection string from .env
mongo_uri = os.environ.get('MONGO_URI')
if not mongo_uri:
    raise ValueError("MONGO_URI is not set in the .env file")

mongo_client = MongoClient(mongo_uri)
db = mongo_client['medication_reminder']
reminder_collection = db['reminders']

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

        # Add timestamp to the reminder data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reminder_data = {'phone_number': user_phone_number, 'medication_name': medication_name, 'timestamp': timestamp}

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

        # Store the reminder in MongoDB with the timestamp
        reminder_collection.insert_one({'timestamp': timestamp, 'reminder_data': reminder_data})


        return jsonify({'message_sid': message.sid}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API endpoint to get reminder history
@app.route('/get-reminders', methods=['GET'])
def get_reminders():
    try:
        reminders = list(reminder_collection.find({}, {'_id': 0}))
        return jsonify(reminders), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to delete logs for a specific medication
@app.route('/delete-logs', methods=['POST'])
def delete_logs():
    try:
        data = request.get_json()
        medication_name = data.get('medication_name')

        # Delete logs for the specified medication
        result = reminder_collection.delete_many({'reminder_data.medication_name': medication_name})

        return jsonify({'message': f'Deleted {result.deleted_count} logs for {medication_name}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
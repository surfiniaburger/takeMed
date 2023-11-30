
![Alt text](image.png)


Medication reminder App is an app to help young souls remind their everlasting seniors to take their medication.

The app as a React Frontend, Python (Flask) Backend, Twilio as a text messenger, taipy as CI/CD pipeline and Auth0 for user authentication.

Once you power the react app with  `npm start`, start the redis server with `redis-server`, and  you run `cd backend && waitress-serve --host=127.0.0.1 --port=5000 app:app` , everything afterwards is seemlessly straightforward. Don't forget to install all dependencies by opening two seperate terminals
 ```npm install```

  and

  ```cd backend && pipenv shell && pipenv install```

## Steps

- If you don't have a twilio account make sure you sign up for a free trial account.
- Login to the takeMed app with your Google account or preferred provider.
- Enter your Love one phone number and the medication.
- Click send reminder.
- Within minutes, your loved one recieves a text.
- Navigate to Reminder log to view a list of previous reminders with their time stamps.
- Delete Previous logs to save cost of scaling to larger database volumes.

![Alt text](<Screenshot (209)-1.png>)
![Alt text](<Screenshot 2023-11-18 at 01.42.17-1.png>)
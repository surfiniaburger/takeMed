// ReminderLog.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './comp.css'

function ReminderLog() {
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    const fetchReminders = async () => {
      try {
        const response = await axios.get('/get-reminders'); // Add a new endpoint in your Flask app to fetch reminders
        setReminders(response.data);
      } catch (error) {
        console.error('Error fetching reminders:', error);
      }
    };

    fetchReminders();
  }, []);

  const fetchReminders = async () => {
    try {
      const response = await axios.get('/get-reminders');
      setReminders(response.data);
    } catch (error) {
      console.error('Error fetching reminders:', error);
    }
  };

  const handleDelete = async (medicationName) => {
    try {
      await axios.post('/delete-logs', { medication_name: medicationName });
      fetchReminders(); // Refresh the reminders after deletion
    } catch (error) {
      console.error('Error deleting logs:', error);
    }
  };

  return (
    <div className="reminder-log">
      <h2>Reminder Log</h2>
      <ul>
        {reminders.map((reminder, index) => (
          <li key={index}>
             {`Medication: ${reminder.reminder_data?.medication_name || 'N/A'}, 
              Phone Number: ${reminder.reminder_data?.phone_number || 'N/A'}, 
              Timestamp: ${reminder.timestamp ? new Date(reminder.timestamp).toLocaleString() : 'N/A'}`}
            <button onClick={() => handleDelete(reminder.reminder_data.medication_name)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReminderLog;

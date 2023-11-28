import React, { useState, useEffect, useCallback } from 'react';
import { useAuth0 } from '@auth0/auth0-react';
import axios from 'axios';
import './App.css';
import LogoutButton from './LogoutButton';


function MedForm() {
      const { isAuthenticated } = useAuth0();
      const [phoneNumber, setPhoneNumber] = useState('');
      const [medicationName, setMedicationName] = useState('');
      const [submitForm, setSubmitForm] = useState(false);

      const handleSendReminder = useCallback(async () => {
        // Your logic for sending reminders
        try {
          // Prepare data for the POST request
          const requestData = {
            phone_number: phoneNumber,
            medication_name: medicationName,
          };
          // Send POST request to Flask backend
          const response = await axios.post('/send-reminder', requestData);
          console.log('Request sent to backend:', response.data);

          // Reset form fields after sending the reminder
          setPhoneNumber('');
          setMedicationName('');
        } catch (error) {
          console.error('Error sending reminder:', error);
        }
      }, [medicationName, phoneNumber]);

      const handleSubmit = (e) => {
        e.preventDefault();
        // Set submitForm to true to trigger useEffect
        setSubmitForm(true);
      };
      useEffect(() => {
        // This effect will run when the component mounts
        if (submitForm) {
            handleSendReminder();
            // Reset submitForm state after sending the reminder
            setSubmitForm(false);
          }
        // Cleanup function (if needed)
        return () => {
          // Perform any cleanup here (if needed)
        };
      }, [handleSendReminder, submitForm]); // Include handleSendReminder in the dependency array
      const isFormFilled = phoneNumber !== '' && medicationName !== '';
      return (
        isAuthenticated && (
          <div className="app-container">
            <LogoutButton/>
          <h1>Medication Reminder App</h1>
          <form className="reminder-form" onSubmit={handleSubmit}>
            <label htmlFor="phoneNumber">Phone Number:</label>
            <input
              type="text"
              id="phoneNumber"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
              placeholder="Enter your phone number"
            />
            <label htmlFor="medicationName">Medication Name:</label>
            <input
              type="text"
              id="medicationName"
              value={medicationName}
              onChange={(e) => setMedicationName(e.target.value)}
              placeholder="Enter the medication name"
            />
            <button type='submit' disabled={!isFormFilled}>Set Reminder</button>
          </form>
        </div>
          )
      )
}

export default MedForm;
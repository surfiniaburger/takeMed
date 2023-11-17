import MedForm from './MedForm';

import React from 'react';
import LoginButton from './LoginButton';
import LogoutButton from './LogoutButton';


function App() {
  return (
    <div className="App">
      <h1>Auth0 Login</h1>
      <LoginButton/>
      <LogoutButton/>
      <MedForm />
    </div>
  );
}

export default App;

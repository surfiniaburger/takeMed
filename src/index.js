import React from 'react';
import { createRoot } from 'react-dom/client';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App';

const root = createRoot(document.getElementById('root'));
const domain_name = process.env.REACT_APP_AUTH0_DOMAIN
const client_Id = process.env.REACT_APP_AUTH0_CLIENT_ID

root.render(
<Auth0Provider
    domain= {domain_name}
    clientId= {client_Id}
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
    <App />
  </Auth0Provider>,
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals


import React from "react";

import blue from "../assets/blue.svg";

const Hero = () => (
  <div className="text-center hero my-5">
    <img className="mb-3 app-logo" src={blue} alt="blue" width="120" />
    <h1 className="mb-4">Medication Reminder Project</h1>

    <p className="lead">
      Remind your loved ones to take their medication as at when due.
    </p>
  </div>
);

export default Hero;

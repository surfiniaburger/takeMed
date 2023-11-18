import React from "react";
import blue from "../assets/blue.svg"

const Footer = () => (
  <footer className="bg-light p-3 text-center">
    
    <div className="blue">
    <img src={blue} alt="blue" width={70} height={70} />
  </div>
    <p>
       © surfiniaburger
    </p>
  </footer>
);

export default Footer;

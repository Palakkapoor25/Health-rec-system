// App.js
import React from 'react';
import './App.css';

const App = () => {
  return (
    <div className="App">
      {/* Header */}
      <header className="header">
        <div className="container">
          <h1 className="logo">AI Health Recommendations</h1>
          <nav className="navbar">
            <ul className="nav-menu">
              <li className="nav-item"><a href="#diagnosis">Diagnosis</a></li>
              <li className="nav-item"><a href="#breast-cancer">Breast Cancer</a></li>
              <li className="nav-item"><a href="#diabetes">Diabetes</a></li>
              <li className="nav-item"><a href="#lung-cancer">Lung Cancer</a></li>
              <li className="nav-item"><a href="#heart-disease">Heart Disease</a></li>
              <li className="nav-item"><a href="#contact">Contact</a></li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero-section">
        <div className="container">
          <h2 className="hero-title">Your Personalized Health Advisor Powered by AI</h2>
          <p className="hero-subtitle">Welcome to our AI-powered health recommendation platform. Get personalized recommendations on medicines, precautions, workouts, and more.</p>
          <img className="hero-image" src="https://media.giphy.com/media/h2idClp1Fbssk3lPlX/giphy.gif" alt="Virtual Health Assistant" />
          <button className="hero-button">Get Started</button>
        </div>
      </section>

      {/* Diagnosis Section */}
      <section id="diagnosis" className="diagnosis-section">
        <div className="container">
          <h2 className="section-title">Diagnosis Using Symptoms</h2>
          <p>Enter your symptoms below to receive personalized recommendations:</p>
          <form className="symptoms-form">
            <input type="text" placeholder="Enter symptoms..." />
            <button type="submit">Diagnose</button>
          </form>
          <div className="diagnosis-results">
            {/* Display diagnosis results dynamically */}
            <p>Diagnosis results go here...</p>
          </div>
        </div>
      </section>

      {/* Breast Cancer Detection Section */}
      <section id="breast-cancer" className="breast-cancer-section">
        <div className="container">
          <h2 className="section-title">Breast Cancer Detection</h2>
          <p>Upload your mammogram or enter details for breast cancer detection:</p>
          <form className="breast-cancer-form">
            <input type="file" accept=".jpg, .jpeg, .png" />
            <button type="submit">Detect Breast Cancer</button>
          </form>
          <div className="breast-cancer-results">
            {/* Display breast cancer detection results dynamically */}
            <p>Breast cancer detection results go here...</p>
          </div>
        </div>
      </section>

      {/* Diabetes Detection Section */}
      <section id="diabetes" className="diabetes-section">
        <div className="container">
          <h2 className="section-title">Diabetes Detection</h2>
          <p>Enter your blood glucose levels for diabetes detection:</p>
          <form className="diabetes-form">
            <input type="number" placeholder="Enter blood glucose level..." />
            <button type="submit">Detect Diabetes</button>
          </form>
          <div className="diabetes-results">
            {/* Display diabetes detection results dynamically */}
            <p>Diabetes detection results go here...</p>
          </div>
        </div>
      </section>

      {/* Lung Cancer Detection Section */}
      <section id="lung-cancer" className="lung-cancer-section">
        <div className="container">
          <h2 className="section-title">Lung Cancer Detection</h2>
          <p>Upload your lung scan or enter details for lung cancer detection:</p>
          <form className="lung-cancer-form">
            <input type="file" accept=".jpg, .jpeg, .png" />
            <button type="submit">Detect Lung Cancer</button>
          </form>
          <div className="lung-cancer-results">
            {/* Display lung cancer detection results dynamically */}
            <p>Lung cancer detection results go here...</p>
          </div>
        </div>
      </section>

      {/* Heart Disease Detection Section */}
      <section id="heart-disease" className="heart-disease-section">
        <div className="container">
          <h2 className="section-title">Heart Disease Detection</h2>
          <p>Enter your heart health metrics for heart disease detection:</p>
          <form className="heart-disease-form">
            <input type="number" placeholder="Enter heart rate..." />
            <input type="number" placeholder="Enter blood pressure..." />
            <button type="submit">Detect Heart Disease</button>
          </form>
          <div className="heart-disease-results">
            {/* Display heart disease detection results dynamically */}
            <p>Heart disease detection results go here...</p>
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="contact-section">
        <div className="container">
          <h2 className="section-title">Contact Us</h2>
          <p>Have questions or need support? Reach out to us.</p>
          <ul>
            <li>Email: contact@healthai.com</li>
            <li>Phone: +1 (123) 456-7890</li>
          </ul>
          <div className="map">
            {/* Interactive map integration can be added here */}
            <p>Map placeholder</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <p>&copy; 2024 AI Health Recommendations. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;

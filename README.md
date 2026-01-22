# Bruteforce Defense Lab

An educational cybersecurity project that demonstrates how brute-force login attacks work and how applications can detect and defend against them using account lockout mechanisms and logging.

This project runs locally and is intended strictly for learning and demonstration purposes.

---

## 🔍 Project Overview

Brute-force attacks are a common threat against authentication systems.  
This lab simulates:

- A vulnerable login endpoint
- A brute-force attack using multiple password attempts
- Defensive mechanisms such as:
  - Failed login tracking
  - Account lockout after repeated failures
  - Security event logging

The goal is to understand both the **attack pattern** and the **defensive response**.

---

## 🛠️ Technologies Used

- Python 3
- Flask (for the login server)
- Requests (for attack simulation)

---

## 📁 Project Structure

bruteforce-defense-lab/
│
├── app.py # Flask login server with security controls
├── attacker.py # Script simulating a brute-force attack
├── users.py # Mock user database and lockout configuration
├── logs.txt # Security logs (generated at runtime, ignored by Git)
├── .gitignore
└── README.md


---

## ⚙️ How It Works

### 1. Login Server (`app.py`)
- Exposes a `/login` endpoint
- Tracks failed login attempts per user
- Locks the account after a predefined number of failures
- Logs all security events to a log file

### 2. Attack Simulation (`attacker.py`)
- Sends multiple login attempts with common passwords
- Mimics a brute-force attack pattern
- Triggers the account lockout mechanism

### 3. Logging
- Every login attempt is logged with a timestamp
- Successful logins, failures, and lockouts are recorded
- Demonstrates the importance of monitoring and audit trails

---

## ▶️ How to Run the Project

### Install dependencies
```bash
pip install flask requests
```

### Start the login server
```bash
pip install flask requests
```

### Run the attack simulation (in a new terminal)
```bash
python attacker.py
```

### View logs

Open logs.txt to observe:
- Failed login attempts
- Account lockout events
- Successful or blocked access

---

🚨 Disclaimer

This project is for educational purposes only.
It runs on localhost and does not target real systems or accounts.

---

## Created By

**Pratima Narang**  
[@cybersighzero](https://github.com/cybersighzero)

Feedback or ideas? Drop an [issue](https://github.com/cybersighzero/WeakSauce/issues) or submit a pull request!

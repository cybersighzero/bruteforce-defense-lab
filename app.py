from flask import Flask, request, jsonify
from users import users, MAX_ATTEMPTS
from datetime import datetime

app = Flask(__name__)

def log_event(message):
    with open("logs.txt", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

@app.route("/")
def home():
    return "Bruteforce Defense Lab Running ;)"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        log_event(f"Unknown user attempt: {username}")
        return jsonify({"status": "fail"}), 401

    user = users[username]

    if user["locked"]:
        log_event(f"LOCKED account login attempt: {username}")
        return jsonify({"status": "locked"}), 403

    if password == user["password"]:
        user["failed_attempts"] = 0
        log_event(f"SUCCESS login: {username}")
        return jsonify({"status": "success"}), 200

    user["failed_attempts"] += 1
    log_event(f"FAILED login {user['failed_attempts']} for {username}")

    if user["failed_attempts"] >= MAX_ATTEMPTS:
        user["locked"] = True
        log_event(f"ACCOUNT LOCKED: {username}")

    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(debug=True)

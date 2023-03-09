import requests, json

with open("config.json") as f:
    config = json.load(f)
    key = config.get('beta.snusbase')

print("""[1] Password Lookup\n[2] Hash Search""")
choice = input("Choice: ")

def passwordsearch():
    password = input("Password: ")
    r = requests.get(f"https://beta.snusbase.com/v1/password/{password}", headers={"authorization":f"{key}"})
    res = r.json()
    print(res)

def hashsearch():
    hash = input("Hash: ")
    r = requests.get(f"https://beta.snusbase.com/v1/hash/{hash}", headers={"authorization":f"{key}"})
    res = r.json()
    print(res)
if choice == "1":
    passwordsearch()
elif choice == "2":
    hashsearch()
else:
    print("Invalid Choice")
import requests, json

with open("config.json") as f:
    config = json.load(f)
    key = config.get('beta.snusbase')

print("""[1] Password Lookup\n[2] Hash Search\n[3] IP Information""")
choice = input("Choice: ")

def ipsearch():
    ip = input("IP Address: ")
    r = requests.get(f"https://beta.snusbase.com/v1/whois/{ip}", headers={"authorization":f"{key}"})
    res = r.json()
    print(f"As: {res['as']}\nCity: {res['city']}\nCountry: {res['country']}\nCountry Code: {res['countryCode']}\nISP: {res['isp']}\nMobile: {res['mobile']}\nOrganization: {res['org']}\nProxy: {res['proxy']}\nRegion: {res['region']}\nState: {res['regionName']}\nZip: {res['zip']}")

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
elif choice == "3":
    ipsearch()
else:
    print("Invalid Choice")
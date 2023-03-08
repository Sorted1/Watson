import requests

bin = input("BIN Number: ")

def check(bin):
    r = requests.get(f"https://lookup.binlist.net/{bin}")
    res = r.json()
    print(f"Length: {res['number']['length']}\nLuhn: {res['number']['luhn']}\nScheme: {res['scheme']}\nType: {res['type']}\nCountry: {res['country']['name']}\nLatitude: {res['country']['latitude']}\nLongitude: {res['country']['longitude']}")

check(bin)
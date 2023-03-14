import requests

vat = input("Enter VAT: ")

def search(vat):
    r = requests.get(f"https://api.vatcomply.com/vat?vat_number={vat}")
    res = r.json()
    print(f"\nNumber: {res['vat_number']}\nName: {res['name']}\nAddress: {res['address']} \nCountry: {res['country_code']}")

search(vat)
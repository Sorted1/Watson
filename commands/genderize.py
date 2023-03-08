import requests

name = input("First Name: ")

def genderize(name):
    r = requests.get(f"https://api.genderize.io?name={name}")
    res = r.json()
    print(f"Name: {res['name']}\nGender: {res['gender']}\nProbability: {res['probability']}")

genderize(name)
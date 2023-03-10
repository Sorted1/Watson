import requests

def reversedns():
    query = input("Enter A Domain Or IP: ")
    url = f"https://api.hackertarget.com/reversedns/?q={query}"
    response = requests.get(url)
    data = response.text
    print(data)

reversedns()
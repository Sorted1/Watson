import requests

ip = input("IP: ")
def ipinfo(ip):
    response = requests.get(f"http://ipwho.is/{ip}")
    if response.status_code != 200:
        print(f"Failed to retrieve IP information for {ip}. Response status code: {response.status_code}")
    else:
        res = response.json()
        typ = res["type"]
        cont = res["continent"]
        cou = res["country"]
        region = res["region"]
        city = res["city"]
        postal = res["postal"]
        print(f"===========\nIP: {ip}\nType: {typ}\nContinent: {cont}\nCountry: {cou}\nRegion: {region}\nCity: {city}\nPostal: {postal}")
ipinfo(ip)
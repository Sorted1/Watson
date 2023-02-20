import requests

def ipinfo(ip):
    api_url = f"http://ipwho.is/{ip}"
    response = requests.get(api_url)
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
        print(f"IP: {ip}\nType: {typ}\nContinent: {cont}\nCountry: {cou}\nRegion: {region}\nCity: {city}\nPostal: {postal}")

# Code for calling function - Dont run with this code below in file
  
# import ipgeolocation

# ip_address = input("Enter an IPv4 address: ")
# ip_info = ipgeolocation.get_ip_info(ip_address)

# if ip_info is not None:
#     print(f"{ip_info['ip_address']} - {ip_info['continent_name']} - {ip_info['state_prov']} - {ip_info['district']} - {ip_info['city']} - {ip_info['zipcode']} - {ip_info['asn']} Request Finished!")
# else:
#     print("Error: Failed to get IP information.")

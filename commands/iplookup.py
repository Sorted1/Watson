import socket
import re

def ipinfo(ip):
    whois_server = 'whois.arin.net'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whois_server, 43))
    s.sendall(ip_address.encode('utf-8') + b"\r\n")
    response = b""
    while True::
            data = s.recv(4096)
            response += data
            if not data:
                break
            s.close()
            response = response.decode('utf-8')
            org_name = re.search(r'OrgName: *([^\n\r]*)', response)
            org_name = org_name.group(1).strip() if org_name else "Not found"
            city = re.search(r'City: *([^\n\r]*)', response)
            city = city.group(1).strip() if city else "Not found"
            State = re.search(r'State: *([^\n\r]*)', response)
            State = state.group(1).strip() if state else "Not found"
            country = re.search(r'Country: *([^\n\r]*)', response)
            country = country.group(1).strip() if country else "Not found"
            
            return {
                "org_name": org_name,
                "city": city,
                "state": state,
                "country": country
            }

#Example
ip = "8.8.8.8"
result = ipinfo(ip)
print("IP Address:", ip)
print("Organization name:", result["org_name"])
print("City:", result["city"])
print("State:", result["state"])
print("Country:", result["country"])

import requests, colorama, json
from colorama import Fore

with open("config.json") as f:
    config = json.load(f)
    key = config.get('carrierkey')


    banner = f"""
    {Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}█████{Fore.WHITE}╗ {Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}██{Fore.WHITE}╗{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██████{Fore.WHITE}╗      {Fore.RED}██████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╗     {Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██████{Fore.WHITE}╗ {Fore.RED}██{Fore.WHITE}╗  {Fore.RED}██{Fore.WHITE}╗{Fore.RED}
   ██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗    {Fore.RED}██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}╔════╝{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║ {Fore.RED}██{Fore.WHITE}╔╝
   {Fore.RED}██{Fore.WHITE}║     {Fore.RED}███████{Fore.WHITE}║{Fore.RED}██████{Fore.WHITE}╔╝{Fore.RED}██████{Fore.WHITE}╔╝{Fore.RED}██{Fore.WHITE}║{Fore.RED}█████{Fore.WHITE}╗  {Fore.RED}██████{Fore.WHITE}╔╝    {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}║     {Fore.RED}█████{Fore.WHITE}╗  {Fore.RED}██████{Fore.WHITE}╔╝{Fore.RED}█████{Fore.WHITE}╔╝ 
   {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}╔══╝  {Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗    {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}║     {Fore.RED}██{Fore.WHITE}╔══╝  {Fore.RED}██{Fore.WHITE}╔══{Fore.RED}██{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}╔═{Fore.RED}██{Fore.WHITE}╗ 
   ╚{Fore.RED}██████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║    ╚{Fore.RED}██████{Fore.WHITE}╗{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}███████{Fore.WHITE}╗{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}║{Fore.RED}██{Fore.WHITE}║  {Fore.RED}██{Fore.WHITE}╗
    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ 
──────────────────────────────────────────────────────────────────────────────────────────────────── """

    txt = banner.center(100)

    print(txt)

    #Issue atm is i think the api is just not working in this use case? maybe im formatting the numbers wrong 
    def get_carrier(phone_number):
        api_url = f"https://ipqualityscore.com/api/json/phone/{key}/1{phone_number}"
        response = requests.get(api_url)
        if response.status_code != 200:
            print(f"Failed to retrieve carrier information for {phone_number}. Response status code: {response.status_code}")
        else:
            res = response.json()
            cars = res["carrier"]
            print(f"[{Fore.GREEN}+{Fore.RESET}] {phone_number} : {cars}")
            carrier = response.json()["carrier"]
            return carrier
    phone_number = input("Phone Number: ")
    if phone_number == "":
        print("Please Enter a phone number")
    else:
        get_carrier(phone_number)
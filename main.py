# -*- coding: utf-8 -*-
import os, colorama
from colorama import Fore
import requests, json
from os import system


def clear():
    os.system("cls")

clear()
system('mode con: cols=100 lines=30')
def banner():
    print("")
    print(f"                      {Fore.RED}██{Fore.RESET}╗    {Fore.RED}██{Fore.RESET}╗ {Fore.RED}█████{Fore.RESET}╗ {Fore.RED}████████{Fore.RESET}╗{Fore.RED}███████{Fore.RESET}╗ {Fore.RED}██████{Fore.RESET}╗ {Fore.RED}███{Fore.RESET}╗   {Fore.RED}██{Fore.RESET}╗".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║    {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}╗╚══{Fore.RED}██{Fore.RESET}╔══╝{Fore.RED}██{Fore.RESET}╔════╝{Fore.RED}██{Fore.RESET}╔═══{Fore.RED}██{Fore.RESET}╗{Fore.RED}████{Fore.RESET}╗  {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║ {Fore.RED}█{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║{Fore.RED}███████{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔{Fore.RED}██{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║{Fore.RED}███{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   ╚════{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║╚{Fore.RED}██{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RESET}╚{Fore.RED}███{Fore.RESET}╔{Fore.RED}███{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║  {Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}║╚{Fore.RED}██████{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║ ╚{Fore.RED}████{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"{Fore.RESET}    ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝".center(os.get_terminal_size().columns))
    print(f"[1] Carrier Clerk [2] Email Validator [3] IP InfoMaster".center(os.get_terminal_size().columns))
    print("────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("")
banner()
choice = input(f"{Fore.RED}Choice: {Fore.RESET}")
if choice == "1":
    clear()
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
if choice == "2":
  clear()
  with open("config.json") as f:
      config = json.load(f)
      key = config.get('emailkey')
  email = input("Email: ")
  def check_email(email):
    api_url = f"https://ipqualityscore.com/api/json/email/{key}/{email}"
    response = requests.get(api_url)
    if response.status_code != 200:
        print(f"Failed to retrieve email information for {email}. Response status code: {response.status_code}")
    else:
      res = response.json()
      ear = res["valid"]
      dispo = res["disposable"]
      fs = res["fraud_score"]
      leaked = res["leaked"]
      print(f"{email} | Valid: {ear} | Disposable: {dispo} | Fraud Score: {fs} | Leaked: {leaked}")
  check_email(email)
if choice == "3":
    clear()
    ip = input("Insert IP: ")
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
    ipinfo(ip)
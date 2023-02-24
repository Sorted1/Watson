# -*- coding: utf-8 -*-
import os, colorama
from colorama import Fore
import requests, json
from os import system
import modules as modules
import importlib

path = './modules'
files_no_ext = [".".join(f.split(".")[:-1]) for f in os.listdir(path) if os.path.isfile(f)]


def clear():
    os.system("cls")

clear()
system('mode con: cols=100 lines=30')
def homeban():
    print("")
    print(f"                      {Fore.RED}██{Fore.RESET}╗    {Fore.RED}██{Fore.RESET}╗ {Fore.RED}█████{Fore.RESET}╗ {Fore.RED}████████{Fore.RESET}╗{Fore.RED}███████{Fore.RESET}╗ {Fore.RED}██████{Fore.RESET}╗ {Fore.RED}███{Fore.RESET}╗   {Fore.RED}██{Fore.RESET}╗".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║    {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}╗╚══{Fore.RED}██{Fore.RESET}╔══╝{Fore.RED}██{Fore.RESET}╔════╝{Fore.RED}██{Fore.RESET}╔═══{Fore.RED}██{Fore.RESET}╗{Fore.RED}████{Fore.RESET}╗  {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║ {Fore.RED}█{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║{Fore.RED}███████{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔{Fore.RED}██{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║{Fore.RED}███{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   ╚════{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║╚{Fore.RED}██{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RESET}╚{Fore.RED}███{Fore.RESET}╔{Fore.RED}███{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║  {Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}║╚{Fore.RED}██████{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║ ╚{Fore.RED}████{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"{Fore.RESET}    ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝".center(os.get_terminal_size().columns))
    print(f"Type Help To See All Commands".center(os.get_terminal_size().columns))
    print("────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("")
homeban()

def banner():
    print("")
    print(f"                      {Fore.RED}██{Fore.RESET}╗    {Fore.RED}██{Fore.RESET}╗ {Fore.RED}█████{Fore.RESET}╗ {Fore.RED}████████{Fore.RESET}╗{Fore.RED}███████{Fore.RESET}╗ {Fore.RED}██████{Fore.RESET}╗ {Fore.RED}███{Fore.RESET}╗   {Fore.RED}██{Fore.RESET}╗".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║    {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}╗╚══{Fore.RED}██{Fore.RESET}╔══╝{Fore.RED}██{Fore.RESET}╔════╝{Fore.RED}██{Fore.RESET}╔═══{Fore.RED}██{Fore.RESET}╗{Fore.RED}████{Fore.RESET}╗  {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║ {Fore.RED}█{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║{Fore.RED}███████{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔{Fore.RED}██{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RED}██{Fore.RESET}║{Fore.RED}███{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   ╚════{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║╚{Fore.RED}██{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"                      {Fore.RESET}╚{Fore.RED}███{Fore.RESET}╔{Fore.RED}███{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║  {Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}║╚{Fore.RED}██████{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║ ╚{Fore.RED}████{Fore.RESET}║".center(os.get_terminal_size().columns))
    print(f"{Fore.RESET}    ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝".center(os.get_terminal_size().columns))
    print("────────────────────────────────────────────────────────────────────────────────────────────────────")
    print("")
    

    

while True:
    maininput = input(f'[{Fore.RED}Terminator{Fore.RESET}]~: ')
    if maininput == 'HELP' or maininput == 'help' or maininput == '?':
        print(f"""Commands:\n=========""")
        for root, dirs, files in os.walk('./modules'):
            for file in files:
                if file.endswith('.py'):
                    os.path.basename(file).split('.')[0]
                    print(os.path.basename(file).split('.')[0])
    else:
        try:
            importlib.import_module("modules."+maininput, package=None)
        except ImportError:
            print("Command Not Found In Modules!")




# if maininput == "1":
#     clear()
#     banner()
#     import modules.phonepriest
    
# if maininput == "2":
#   clear()
#   banner()
#   import modules.emailcheck

# if maininput == "3":
#     clear()
#     banner()
#     import modules.ipgeolocation as ipgeolocation
#     ip_address = input("Enter an IPv4 address: ")
#     ip_info = ipgeolocation.ipinfo(ip_address)

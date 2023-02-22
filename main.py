# -*- coding: utf-8 -*-
import os, colorama
from colorama import Fore
import requests, json
from os import system


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
    print(f"[1] Phone Priest [2] Email Validator [3] IP InfoMaster".center(os.get_terminal_size().columns))
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

choice = input(f"{Fore.RED}Choice: {Fore.RESET}")
if choice == "1":
    clear()
    banner()
    import modules.phonepriest
if choice == "2":
  clear()
  banner()
  import modules.emailcheck
if choice == "3":
    clear()
    banner()
    import modules.ipgeolocation as ipgeolocation
    ip_address = input("Enter an IPv4 address: ")
    ip_info = ipgeolocation.ipinfo(ip_address)

import os, colorama
from colorama import Fore
import shutil
from os import system


def clear():
    os.system("cls")

clear()
system('mode con: cols=100 lines=30')
print("")
print(f"                    {Fore.RED}██{Fore.RESET}╗    {Fore.RED}██{Fore.RESET}╗ {Fore.RED}█████{Fore.RESET}╗ {Fore.RED}████████{Fore.RESET}╗{Fore.RED}███████{Fore.RESET}╗ {Fore.RED}██████{Fore.RESET}╗ {Fore.RED}███{Fore.RESET}╗   {Fore.RED}██{Fore.RESET}╗".center(os.get_terminal_size().columns))
print(f"                    {Fore.RED}██{Fore.RESET}║    {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}╗╚══{Fore.RED}██{Fore.RESET}╔══╝{Fore.RED}██{Fore.RESET}╔════╝{Fore.RED}██{Fore.RESET}╔═══{Fore.RED}██{Fore.RESET}╗{Fore.RED}████{Fore.RESET}╗  {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
print(f"                    {Fore.RED}██{Fore.RESET}║ {Fore.RED}█{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║{Fore.RED}███████{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔{Fore.RED}██{Fore.RESET}╗ {Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
print(f"                    {Fore.RED}██{Fore.RESET}║{Fore.RED}███{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}╔══{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   ╚════{Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║{Fore.RED}██{Fore.RESET}║╚{Fore.RED}██{Fore.RESET}╗{Fore.RED}██{Fore.RESET}║".center(os.get_terminal_size().columns))
print(f"                    {Fore.RESET}╚{Fore.RED}███{Fore.RESET}╔{Fore.RED}███{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║  {Fore.RED}██{Fore.RESET}║   {Fore.RED}██{Fore.RESET}║   {Fore.RED}███████{Fore.RESET}║╚{Fore.RED}██████{Fore.RESET}╔╝{Fore.RED}██{Fore.RESET}║ ╚{Fore.RED}████{Fore.RESET}║".center(os.get_terminal_size().columns))
print(f"{Fore.RESET} ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝".center(os.get_terminal_size().columns))
print("────────────────────────────────────────────────────────────────────────────────────────────────────")
print("")
choice = input(f"{Fore.RED}Choice: {Fore.RESET}")
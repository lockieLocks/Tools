import requests
import time
import os
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def the_ascii_art():
    ascii_art = f""" {Fore.YELLOW}
   _____ ________________   ____  __________  ________  __________________   __________  ___   ________ __ __________ 
  / ___//  _/_  __/ ____/  / __ \/ ____/ __ \/  _/ __ \/ ____/ ____/_  __/  /_  __/ __ \/   | / ____/ //_// ____/ __ \
  \__ \ / /  / / / __/    / /_/ / __/ / / / // // /_/ / __/ / /     / /      / / / /_/ / /| |/ /   / ,<  / __/ / /_/ /
 ___/ // /  / / / /___   / _, _/ /___/ /_/ // // _, _/ /___/ /___  / /      / / / _, _/ ___ / /___/ /| |/ /___/ _, _/ 
/____/___/ /_/ /_____/  /_/ |_/_____/_____/___/_/ |_/_____/\____/ /_/      /_/ /_/ |_/_/  |_\____/_/ |_/_____/_/ |_|                     
"""
    print(ascii_art)

def site_redirect_tracker():
    while True:
        clear()
        the_ascii_art()
        site = input(f"Enter Site [https AT START]{Fore.LIGHTWHITE_EX}>>{Fore.YELLOW}")
        try:
            r = requests.get(site)
            input(f"\n{Fore.LIGHTWHITE_EX}[{Fore.YELLOW}+{Fore.LIGHTWHITE_EX}]{Fore.YELLOW} {site} is redirecting to {r.url}...")
        except requests.exceptions.ConnectionError:
            input(f"\n{Fore.LIGHTWHITE_EX}[{Fore.YELLOW}-{Fore.LIGHTWHITE_EX}]{Fore.YELLOW} {site} is not a valid site...")

site_redirect_tracker()
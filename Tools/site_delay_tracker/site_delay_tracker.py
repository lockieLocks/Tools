import os
import requests
import time
from colorama import Fore

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def the_ascii_art():
    ascii_art = """
   _____ ________________   ____  ________    _____  __   __________  ___   ________ __ __________ 
  / ___//  _/_  __/ ____/  / __ \/ ____/ /   /   \ \/ /  /_  __/ __ \/   | / ____/ //_// ____/ __ \
  \__ \ / /  / / / __/    / / / / __/ / /   / /| |\  /    / / / /_/ / /| |/ /   / ,<  / __/ / /_/ /
 ___/ // /  / / / /___   / /_/ / /___/ /___/ ___ |/ /    / / / _, _/ ___ / /___/ /| |/ /___/ _, _/ 
/____/___/ /_/ /_____/  /_____/_____/_____/_/  |_/_/    /_/ /_/ |_/_/  |_\____/_/ |_/_____/_/ |_|  
"""
    print(ascii_art)


def site_delay_checker():
    while True:
        clear()
        the_ascii_art()
        url = input(f"Enter URL [https AT START] {Fore.LIGHTWHITE_EX}>>{Fore.LIGHTBLUE_EX}")
        try:
            start = time.time()
            r = requests.get(url)
            end = time.time() - start
            print(f"Response time >> {end:.2f} seconds")
        except Exception as e:
            input(f"Error: {e}")

site_delay_checker()
import os
import requests
from colorama import Fore

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def url_ascii():
    ascii_art = f""" {Fore.CYAN}
 #     # ######  #           #####  #     # ####### ######  ####### ####### #     # ####### ######  
 #     # #     # #          #     # #     # #     # #     #    #    #       ##    # #       #     # 
 #     # #     # #          #       #     # #     # #     #    #    #       # #   # #       #     # 
 #     # ######  #           #####  ####### #     # ######     #    #####   #  #  # #####   ######  
 #     # #   #   #                # #     # #     # #   #      #    #       #   # # #       #   #   
 #     # #    #  #          #     # #     # #     # #    #     #    #       #    ## #       #    #  
  #####  #     # #######     #####  #     # ####### #     #    #    ####### #     # ####### #     # """
    print(ascii_art)

def url_shortener():
    clear()
    url_ascii()
    url = input(f"\nEnter URL to shorten with tinyurl {Fore.LIGHTWHITE_EX}>>{Fore.YELLOW} ")
    try:
        r = requests.get(f"https://tinyurl.com/api-create.php?url={url}")
        print(f"\n[+] Short URL: {r.text}")
    except Exception as e:
        print(f"[x] Error: {e}")
    input("\nPress Enter to continue...")
    url_shortener()

if __name__ == "__main__":
    url_shortener()
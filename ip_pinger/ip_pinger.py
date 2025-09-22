import os
import time
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def the_ascii_art():
    ascii_art = f""" {Fore.LIGHTRED_EX}

888 888~-_        888~-_   888 888b    |  e88~~\  888~~  888~-_   
888 888   \       888   \  888 |Y88b   | d888     888___ 888   \  
888 888    |      888    | 888 | Y88b  | 8888 __  888    888    | 
888 888   /       888   /  888 |  Y88b | 8888   | 888    888   /  
888 888_-~        888_-~   888 |   Y88b| Y888   | 888    888_-~   
888 888           888      888 |    Y888  "88__/  888___ 888 ~-_  
             ----                                                 
"""
    print(ascii_art)

def ip_pinger():
    param = "-n 1" if os.name == "nt" else "-c 1"
    ip = input("Enter Target IP >> ")
    times = int(input(f"How many times? {Fore.LIGHTWHITE_EX}>>{Fore.LIGHTRED_EX} "))
    try:
        for i in range(times):
            os.system(f"ping {param} {ip}")
            time.sleep(1)

    except Exception as e:
        print(f"Error: {e}")
    input(f"Press Enter to return{Fore.LIGHTWHITE_EX}...{Fore.LIGHTRED_EX}")
    main()

def main():
    clear()
    the_ascii_art()
    print(f"                             {Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTWHITE_EX}]{Fore.LIGHTRED_EX} Ping IP")
    option = input("Option >> ")
    if option == '1':
        ip_pinger()
    else:
        print("Returning...")
        time.sleep(0.5)
        main()

if __name__ == '__main__':
    main()


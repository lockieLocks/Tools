import requests
import os
from colorama import Fore

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ascii_art():
    ascii = f""" {Fore.LIGHTMAGENTA_EX}
 _______  _______  ___   _  _______  __    _    ___   __    _  _______  _______ 
|       ||       ||   | | ||       ||  |  | |  |   | |  |  | ||       ||       |
|_     _||   _   ||   |_| ||    ___||   |_| |  |   | |   |_| ||    ___||   _   |
  |   |  |  | |  ||      _||   |___ |       |  |   | |       ||   |___ |  | |  |
  |   |  |  |_|  ||     |_ |    ___||  _    |  |   | |  _    ||    ___||  |_|  |
  |   |  |       ||    _  ||   |___ | | |   |  |   | | | |   ||   |    |       |
  |___|  |_______||___| |_||_______||_|  |__|  |___| |_|  |__||___|    |_______|
"""
    print(ascii)

def get_token_info():
    clear()
    ascii_art()
    token = input("Enter Discord Token >> ")
    try:
        headers = {
            "Authorization": token
        }
        url = "https://discord.com/api/v9/users/@me"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("\nToken is Valid")
            json_dump = input("Would you like to Json Dump [Y or N] >> ")
            json_normal = json_dump.lower().strip()
            if json_normal == 'y':
                print("-" * 25 + "Json Token Dump" + "-" * 25)
                for k, v in data.items():
                    print(f"{k} :3> {v}")
            elif json_normal == 'n':
                print("-" * 25 + "Token Info" + "-" * 25)
                print(f"Username >> {data.get('username', 'N/A')}")
                print(f"ID >> {data.get('id', 'N/A')}")
                print(f"Email >> {data.get('email', 'N/A')}")
                print(f"Phone Number >> {data.get('phone', 'Phone Not Linked')}")
                premium = data.get("premium", 0)
                if premium == 1:
                    print("Nitro = True - Nitro Version >> Classic")
                elif premium == 2:
                    print("Nitro = True - Nitro Version >> Diamond")
                else:
                    print("Nitro = False")
        elif response.status_code == 401:
            print("Invalid Token")
        else:
            print(f"Error - Status Code >> {response.status_code}")
    except Exception as e:
        print(f"Error >> {e}")

if __name__ == "__main__":
    get_token_info()
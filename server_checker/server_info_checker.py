import requests
from colorama import Fore
import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def ascii_art():
    asciii = f""" {Fore.LIGHTRED_EX}
   .dMMMb  dMMMMMP dMMMMb  dMP dMP dMMMMMP dMMMMb        .aMMMb  dMP dMP dMMMMMP .aMMMb  dMP dMP dMMMMMP dMMMMb 
  dMP" VP dMP     dMP.dMP dMP dMP dMP     dMP.dMP       dMP"VMP dMP dMP dMP     dMP"VMP dMP.dMP dMP     dMP.dMP 
  VMMMb  dMMMP   dMMMMK" dMP dMP dMMMP   dMMMMK"       dMP     dMMMMMP dMMMP   dMP     dMMMMK" dMMMP   dMMMMK"  
dP .dMP dMP     dMP"AMF  YMvAP" dMP     dMP"AMF       dMP.aMP dMP dMP dMP     dMP.aMP dMP"AMF dMP     dMP"AMF   
VMMMP" dMMMMMP dMP dMP    VP"  dMMMMMP dMP dMP        VMMMP" dMP dMP dMMMMMP  VMMMP" dMP dMP dMMMMMP dMP dMP                                                                                                                    
"""
    print(asciii)

def server_checker():
    clear()
    ascii_art()
    invite = input(f"Enter Server Code {Fore.LIGHTWHITE_EX}>>{Fore.LIGHTBLUE_EX} ").strip()
    output_option = input("Do you want to save the output to a file? (y/n) >> ").strip().lower()
    if output_option == 'y':
        output = True
    elif output_option == 'n':
        output = False
    try:
        url = requests.get(f"https://discord.com/api/v9/invites/{invite}?withcounts=True")
        data = url.json()
        guild = data['guild']
        print("-" * 25 + "Guild Info" + "-" * 25)
        for key, value in guild.items():
            print(f"{key} :3> {value}")
    except Exception as e:
            print(f"Error >> {e}")
    if output:
        try:
            with open("server_info.txt", "w") as f:
                for key, value in guild.items():
                    f.write(f"{key} :3> {value}\n")
            print("Output saved to server_info.txt")
        except Exception as e:
            print(f"Error saving to file >> {e}")
    else:
        pass
if __name__ == "__main__":
    server_checker()
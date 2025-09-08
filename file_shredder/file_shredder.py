import os
import time
from colorama import Fore

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def ascii_art():
    ascii = f""" {Fore.LIGHTYELLOW_EX}
    _______ __        _____ __                  __    __         
   / ____(_) /__     / ___// /_  ________  ____/ /___/ /__  _____
  / /_  / / / _ \    \__ \/ __ \/ ___/ _ \/ __  / __  / _ \/ ___/
 / __/ / / /  __/   ___/ / / / / /  /  __/ /_/ / /_/ /  __/ /    
/_/   /_/_/\___/   /____/_/ /_/_/   \___/\__,_/\__,_/\___/_/                                                                      
"""
    print(ascii)

def file_shredder():
    clear()
    ascii_art()
    shred_list_option = input("Would you like to use shred_list.txt file paths [Y or N] >> ")
    if shred_list_option.lower().strip() == 'y':
        txt_shredder()
    elif shred_list_option.lower().strip() == 'n':
        pass
    path = input("Drag and Drop File to Shred here >> ")
    try:
        if not os.path.exists(path):
            print("File Not Found")
            file_shredder()
        print("\nFile Found...")
        option = input("Are You Sure you want to proceed [Y or N] >> ")
        option_normal = option.lower().strip()
        if option_normal == 'y':
            output_option = True
        elif option_normal == 'n':
            output_option = False
        else:
            print("Invalid Option...")
            time.sleep(0.5)
            file_shredder()
        if output_option:
            os.remove(path)
            print("Shredding File", end="", flush=True)
            for i in range(5):
                print(".", end="", flush=True)
                time.sleep(0.5)
        else:
            file_shredder()
            print()
    except Exception as e:
        print(f"Error >> {e}")

def txt_shredder():
    shred_list = "shred_list.txt"
    if not os.path.exists(shred_list):
        print("shred_list.txt not found...")
        time.sleep(1)
        file_shredder()
    with open(shred_list, "r") as r:
        paths = r.readlines()
        for line in paths:
            path = line.strip().strip('"')
            if os.path.exists(path):
                try:
                    os.remove(path)
                    print(f"Deleted >> {path} Successfully")
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                print(f"{path} Not Found")

if __name__ == "__main__":
    file_shredder()

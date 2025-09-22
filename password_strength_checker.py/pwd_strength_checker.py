from colorama import Fore
import os

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def ascii_art():
    asciii = f""" {Fore.LIGHTYELLOW_EX}

.sSSSSs.    .sSSS       s.    .sSSSSs.         .sSSSSs.                                                                              
SSSSSSSSSs. SSSSS       SSSs. SSSSSSSSSs.      SSSSSSSSSs. .sSSS SSSSS .sSSSSs.    .sSSSSs.    .sSSS  SSSSS  .sSSSSs.    .sSSSSSSSs. 
S SSS SSSSS S SSS       SSSSS S SSS SSSSS      S SSS SSSSS S SSS SSSSS S SSSSSSSs. S SSSSSSSs. S SSS SSSSS   S SSSSSSSs. S SSS SSSSS 
S  SS SSSSS S  SS       SSSSS S  SS SSSSS      S  SS SSSS' S  SS SSSSS S  SS SSSS' S  SS SSSS' S  SS SSSSS   S  SS SSSS' S  SS SSSS' 
S..SS SSSSS S..SS       SSSSS S..SS SSSSS      S..SS       S..SSsSSSSS S..SS       S..SS       S..SSsSSSSS   S..SS       S..SSsSSSa. 
S:::SsSSSSS S:::S       SSSSS S:::S SSSSS      S:::S SSSSS S:::S SSSSS S:::SSSS    S:::S SSSSS S:::S SSSSS   S:::SSSS    S:::S SSSSS 
S;;;S       S;;;S   S   SSSSS S;;;S SSSSS      S;;;S SSSSS S;;;S SSSSS S;;;S       S;;;S SSSSS S;;;S  SSSSS  S;;;S       S;;;S SSSSS 
S%%%S       S%%%S  SSS  SSSSS S%%%S SSSS'      S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S SSSSS S%%%S  SSSSS  S%%%S SSSSS S%%%S SSSSS 
SSSSS       SSSSSsSS SSsSSSSS SSSSSsS;:'       SSSSSsSSSSS SSSSS SSSSS SSSSSsSS;:' SSSSSsSSSSS SSSSS   SSSSS SSSSSsSS;:' SSSSS SSSSS                                                                                                                                      
"""
    print(asciii)

def check_pwd():
    clear()
    ascii_art()
    pwd = input(f"\nEnter Password to Rate {Fore.LIGHTWHITE_EX}>>{Fore.LIGHTBLUE_EX} ")
    strength = 0
    if any(char.isdigit() for char in pwd):
        strength += 2
    if any(char.isupper() for char in pwd):
        strength += 2
    if any(char.islower() for char in pwd):
        strength += 2
    if any(char in "+=-_)(*&^%$#@!~`;:'/?.>,<\\|)" for char in pwd):
        strength += 2
    if len(pwd) >= 8:
        strength += 2
    print(f"Password is {strength}{Fore.LIGHTWHITE_EX}/10{Fore.LIGHTBLUE_EX}")
    input(f"\nPress Enter to return{Fore.LIGHTWHITE_EX}...{Fore.LIGHTBLUE_EX}")
    clear()
    check_pwd()

if __name__ == "__main__":
    check_pwd()

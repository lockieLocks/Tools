#!/usr/bin/env python3

from threading import local
import requests
import sys
import time
import os
import subprocess
from colorama import Fore
import shutil
import socket

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_all_ips():
    try:
        public_ip = requests.get("https://api.ipify.org?format=text", timeout=5).text.strip()
    except:
        public_ip = "Could not fetch"

    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except:
        hostname = local_ip = "Could not fetch"

    print(f"Public IP >> {public_ip}\nLocal IP >> {local_ip}\nHostname >> {hostname}")
    input("Press Enter to return...")
    network_main()

def ip_pinger_download(run_option, return_to_menu=True, Download_option=True):
    ip_pinger_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/ip_pinger/ip_pinger.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "ip_pinger")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "ip_pinger.py")
    try:
        response = requests.get(ip_pinger_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded ip_pinger.py")
                else:
                    print("Failed to Download File ip_pinger.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':       
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def b64_download(run_option, return_to_menu=True, Download_option=True):
    b64_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/base64/b64.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "base64")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "b64.py")
    try:
        response = requests.get(b64_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded b64.py")
                else:
                    print("Failed to Download File b64.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename]) 
                except Exception as e:
                    print(f"Error >> {e}")    
            else:
                if return_to_menu:
                    print("Returing...")
                    time.sleep(0.5)
                    tools_menu()   
                else:
                    return      
    except Exception as e:
        print(f"Error >> {e}")

def username_lookup_download(run_option, return_to_menu=True, Download_option=True):
    username_lookup_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/username_lookup/username_lookup.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "username_lookup")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "username_lookup.py")
    try:
        response = requests.get(username_lookup_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded username_lookup.py")
                else:
                    print("Failed to Download username_lookup.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename]) 
                except Exception as e:
                    print(f"Error >> {e}")    
            else:
                if return_to_menu:
                    print("Returing...")
                    time.sleep(0.5)
                    tools_menu()   
                else:
                    return      

    except Exception as e:
        print(f"Error >> {e}")
    if return_to_menu:
        input("Press Enter to return...")
        tools_menu()
    else:
        return

def ip_lookup_download(run_option, return_to_menu=True, Download_option=True):
    ip_lookup_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/ip_lookup/ip_lookup.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "ip_lookup")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "ip_lookup.py")
    try:
        response = requests.get(ip_lookup_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded ip_lookup.py")
                else:
                    print("Failed to Download File ip_lookup.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def webhook_mutltitool_download(run_option, return_to_menu=True, Download_option=True):
    webhook_multitool_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/webhook_multitool/webhook_multitool.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "webhook_multitool")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "webhook_multitool.py")
    try:
        response = requests.get(webhook_multitool_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded webhook_multitool.py")
                else:
                    print("Failed to Download File webhook_multitool.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    pass
    except Exception as e:
        print(f"Error >> {e}")

def site_checker(run_option, return_to_menu=True, Download_option=True):
    site_multitool_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/site_multitool/site_multitool.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "site_multitool")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "site_multitool.py")
    try:
        response = requests.get(site_multitool_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded site_checker.py")
                else:
                    print("Failed to Download site_checker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def nitro_gen_download(run_option, return_to_menu=True, Download_option=True):
    site_multitool_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/nitro_generator/nitro_gen.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "nitro_generator")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "nitro_gen.py")
    try:
        response = requests.get(site_multitool_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded nitro_generator.py")
                else:
                    print("Failed to Download File nitro_gen.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def pwd_strength_checker(run_option, return_to_menu=True, Download_option=True):
    pwd_strength_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/password_strength_checker.py/pwd_strength_checker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "password_strength_checker.py")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "pwd_strength_checker.py")
    try:
        response = requests.get(pwd_strength_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded pwd_strength_checker.py")
                else:
                    print("Failed to Download pwd_strength_checker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return

    except Exception as e:
        print(f"Error >> {e}")

def token_validator(run_option, return_to_menu=True, Download_option=True):
    token_validator_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/token_validator/token_validator.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "token_validator")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "token_validator.py")
    file_token = os.path.join(folder_name, "tokens.txt")
    try:
        response = requests.get(token_validator_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded token_validator.py")
                else:
                    print("Falied to Download token_validator.py")
            else:
                print("File Already Exists")
                pass
                if not os.path.exists(file_token):
                    with open(file_token, "w") as t:
                        t.write("put tokens here twin")
        else:
            pass
            if run_option.lower().strip() == 'y':
                try:
                    subprocess.run([sys.executable, filename])
                except Exception as e:
                    print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def server_checker(run_option, return_to_menu=True, Download_option=True):
    server_checker_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/server_checker/server_checker.py"
    tools_folder = "Tools"
    folder_name = os.path.join(tools_folder, "server_checker")
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "server_info_checker.py")
    try:
        response = requests.get(server_checker_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded server_checker.py")
                else:
                    print("Failed to Download server_checker.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def url_shortener(run_option, return_to_menu=True, Download_option=True):
    url_shortener_link = "https://raw.githubusercontent.com/lockieLocks/Tools/main/Tools/url_shortener/url_shortener.py"
    folder_name = "url_shortener"
    os.makedirs(folder_name, exist_ok=True)
    filename = os.path.join(folder_name, "url_shortener.py")
    try:
        response = requests.get(url_shortener_link)
        if Download_option:
            if not os.path.exists(filename):
                if response.status_code == 200:
                    with open(filename, "wb") as file:
                        file.write(response.content)
                        print("Successfully downloaded url_shortener.py")
                else:
                    print("Failed to Download url_shortener.py")
            else:
                print("File Already Exists...")
                pass
        else:
            pass
        if run_option.lower().strip() == 'y':
            try:
                subprocess.run([sys.executable, filename])
            except Exception as e:
                print(f"Error >> {e}")
            else:
                if return_to_menu:
                    print("Returning...")
                    time.sleep(0.5)
                    tools_menu()
                else:
                    return
    except Exception as e:
        print(f"Error >> {e}")

def full_wipe():
    main_dir = os.getcwd()
    for name in os.listdir(main_dir):
        path = os.path.join(main_dir, name)
        if os.path.isdir(path):
            if name.lower() in [".vs", "__pycache__", "main.py", ".git", ".github"]:  
                continue
            shutil.rmtree(path)
            print(f"Deleted All Folders >> {path}")

def full_cleanup(script_name="main.py"):
    github_url = "https://raw.githubusercontent.com/lockieLocks/Multitool/main/main.py"
    temp_script = "_new_main.py"
    batch_file = "_new_file.bat"
    print("Downloading latest version...")
    r = requests.get(github_url)
    if r.status_code == 200:
        full_wipe()
        with open(temp_script, "wb") as f:
            f.write(r.content)
    else:
        print("Falied to download latest version.")
    with open(batch_file, "w") as bf:
        bf.write(f"""
@echo off
move {temp_script} {script_name}
start "" "{sys.executable}" "{script_name}"
del {batch_file}
""")
        print("Restarting script...")
    os.startfile(batch_file)
    sys.exit()

def update():
    main_dir = os.getcwd()
    for name in os.listdir(main_dir):
        path = os.path.join(main_dir, name)
        if os.path.isdir(path):
            if name.lower() in [".vs", "__pycache__", ".git", ".github"]:  
                continue
            shutil.rmtree(path)
            print(f"Deleted All Folders >> {path}")
    print("Redownloading files...")
    time.sleep(0.5)
    ip_lookup_download(run_option='n', return_to_menu=False)
    ip_pinger_download(run_option='n', return_to_menu=False)
    b64_download(run_option='n', return_to_menu=False)
    username_lookup_download(run_option='n', return_to_menu=False)
    webhook_mutltitool_download(run_option='n', return_to_menu=False)
    site_checker(run_option='n', return_to_menu=False)
    pwd_strength_checker(run_option='n', return_to_menu=False)
    token_validator(run_option='n', return_to_menu=False)
    nitro_gen_download(run_option='n', return_to_menu=False)
    server_checker(run_option='n', return_to_menu=False)
    input("\nPress Enter to return...")
    tools_menu()

def install_all():
    ip_lookup_download(run_option='n', return_to_menu=False)
    ip_pinger_download(run_option='n', return_to_menu=False)
    b64_download(run_option='n', return_to_menu=False)
    username_lookup_download(run_option='n', return_to_menu=False)
    webhook_mutltitool_download(run_option='n', return_to_menu=False)
    site_checker(run_option='n', return_to_menu=False)
    pwd_strength_checker(run_option='n', return_to_menu=False)
    nitro_gen_download(run_option='n', return_to_menu=False)
    token_validator(run_option='n', return_to_menu=False)
    server_checker(run_option='n', return_to_menu=False)
    input("\nPress Enter to return...")
    tools_menu()

def tools_ascii():
    ascii = f""" {Fore.RED}

                             ______          __  ___                        
                            /_  __/__  ___  / / / _ \__ _____  ___  ___ ____
                             / / / _ \/ _ \/ / / , _/ // / _ \/ _ \/ -_) __/
                            /_/  \___/\___/_/ /_/|_|\_,_/_//_/_//_/\__/_/                                                   
====================================================================================================
                                   Press b to return to main menu  
                                   Press 99 to Install and Update all tools
                                   Press 404 to Exit
"""
    print(ascii)

def tools_menu():
    clear()
    tools_ascii()
    print("                [------Network Tools------]          [------Utility Tools------]             [------Discord Tools------]")
    print("                     [1] - Ip Lookup                    [4] - B64 Tools                       [7] - Webhook Multitool")
    print("                     [2] - IP Pinger                    [5] - Username Lookup                 [8] - Token Validator")               
    print("                     [3] - Site Multitool               [6] - Password Strength Checker       [9] - Nitro Generator")
    print("                                                                                              [10] - Server Info Checker")
    option = input("Option >> ")
    if option == '1':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        ip_lookup_download(run_option, Download_option=False)
    elif option == '2':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        ip_pinger_download(run_option, Download_option=False)
    elif option == '3':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        site_checker(run_option, Download_option=False)
    elif option == '4':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        b64_download(run_option, Download_option=False)
    elif option == '5':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        username_lookup_download(run_option, Download_option=False)
    elif option == '6':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        pwd_strength_checker(run_option, Download_option=False)
    elif option == '7':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        webhook_mutltitool_download(run_option, Download_option=False)
    elif option == '8':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        token_validator(run_option, Download_option=False)
    elif option == '9':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        nitro_gen_download(run_option, Download_option=False)
    elif option == '10':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        server_checker(run_option, Download_option=False)
    elif option == '99':
        update()
    elif option == '404':
        print("Returning...")
        time.sleep(0.5)
        sys.exit()
    elif option.lower().strip() == 'b':
        print("Returning to main menu...")
        time.sleep(0.5)
        main()
    else:
        print("Invalid Option...")
        time.sleep(0.5)
        clear()
        tools_menu()

def main_ascii():
    ascii = f"""  {Fore.LIGHTMAGENTA_EX}
                   __       __   ______   ______  __    __        __       __  ________  __    __  __    __ 
                  |  \     /  \ /      \ |      \|  \  |  \      |  \     /  \|        \|  \  |  \|  \  |  |
                  | $$\   /  $$|  $$$$$$\ \$$$$$$| $$\ | $$      | $$\   /  $$| $$$$$$$$| $$\ | $$| $$  | $$
                  | $$$\ /  $$$| $$__| $$  | $$  | $$$\| $$      | $$$\ /  $$$| $$__    | $$$\| $$| $$  | $$
                  | $$$$\  $$$$| $$    $$  | $$  | $$$$\ $$      | $$$$\  $$$$| $$  \   | $$$$\ $$| $$  | $$
                  | $$\$$ $$ $$| $$$$$$$$  | $$  | $$\$$ $$      | $$\$$ $$ $$| $$$$$   | $$\$$ $$| $$  | $$
                  | $$ \$$$| $$| $$  | $$ _| $$_ | $$ \$$$$      | $$ \$$$| $$| $$_____ | $$ \$$$$| $$__/ $$
                  | $$  \$ | $$| $$  | $$|   $$ \| $$  \$$$      | $$  \$ | $$| $$     \| $$  \$$$ \$$    $$
                   \$$      \$$ \$$   \$$ \$$$$$$ \$$   \$$       \$$      \$$ \$$$$$$$$ \$$   \$$  \$$$$$$ 
                                                __  _      ___ ___    
                                                 / |_ |\ |  |   | |_| 
                                                /_ |_ | \| _|_  | | |  
-----------------------------------------------------------------------------------------------------------------------
                                |                                                     |
                                |   3:< Welcome to MAIN MENU of lockies multitool >:3 |
                                |         404 - FULL WIPE AND REINSTALL               |
                                |          100 - INSTALL and UPDATE ALL Tools         |
                                |         t  - ALL Tools Runner")                     |
                                -------------------------------------------------------
                                |         d - Discord Tools runner                    |
                                |         n - Network Tools runner                    |
                                |         u - Utillity Tools runner                   |
                                |                 Have Fun :3                         |
                                |_____________________________________________________|"""
    print(ascii)

def main():
    clear()
    main_ascii()
    print("\n                  [1]  - Install Discord Tools = Webhook spammer, Token Validator, Nitro Generator, Server Info Checker")
    print("                  [2]  - Install Network Tools = IP Lookup, IP Pinger, Site Multitool")
    print("                  [3]  - Install Utility Tools = Username lookup, B64 multitool, Pwd Strength Checker")
    print("                  [4]  - Install All tools = All of above")
    print("                  [99] - Exit")
    option = input("Option >> ")
    if option == '1':
        token_validator(run_option='n', return_to_menu=False)
        webhook_mutltitool_download(run_option='n', return_to_menu=False)
        nitro_gen_download(run_option='n', return_to_menu=False)
        server_checker(run_option='n', return_to_menu=False)
        input("Press Enter to return...")
        main()
    elif option == '2':
        ip_lookup_download(run_option='n', return_to_menu=False)
        ip_pinger_download(run_option='n', return_to_menu=False)
        site_checker(run_option='n', return_to_menu=False)
        input("Press Enter to return...")
        main()
    elif option == '3':
        username_lookup_download(run_option='n', return_to_menu=False)
        b64_download(run_option='n', return_to_menu=False)
        pwd_strength_checker(run_option='n', return_to_menu=False)
        input("Press Enter to return...")
        main()
    elif option == '4':
        install_all()
    elif option.lower().strip() == 't':
        tools_menu()
    elif option.lower().strip() == 'd':
        discord_tools_main()
    elif option.lower().strip() == 'u':
        utility_Tools_main()
    elif option.lower().strip() == 'n':
        network_main()
    elif option == '100':
        update()
    elif option == '404':
        full_cleanup()
    elif option == '99':
        print("Peace Out gng...")
        time.sleep(0.5)
        sys.exit()
    else:
        print("Returning")
        time.sleep(0.5)
        main()

def Utility_ascii():
    ascii = f""" {Fore.LIGHTRED_EX}

  _    _ _   _ _ _ _           _______          _     
 | |  | | | (_) (_) |         |__   __|        | |    
 | |  | | |_ _| |_| |_ _   _     | | ___   ___ | |___ 
 | |  | | __| | | | __| | | |    | |/ _ \ / _ \| / __|
 | |__| | |_| | | | |_| |_| |    | | (_) | (_) | \__ |
  \____/ \__|_|_|_|\__|\__, |    |_|\___/ \___/|_|___/
                        __/ |                         
                       |___/                          
                100 - Return to main menu
"""
    print(ascii)

def utility_Tools_main():
    clear()
    Utility_ascii()
    print("                 [1] - Run Username Lookup")
    print("                 [2] - Run B64 Multitool")
    print("                 [3] - Run Password Strength Checker")
    option = input("Option >> ")
    if option == '1':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        username_lookup_download(run_option, Download_option=False)
    elif option == '2':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        b64_download(run_option, Download_option=False)
    elif option == '3':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        pwd_strength_checker(run_option, Download_option=False)
    elif option == '100':
        print("Returning to main menu...")
        main()
    else:
        print("Invalid...")
        time.sleep(0.5)
        utility_Tools_main()


def Network_ascii():
    ascii = f""" {Fore.LIGHTBLUE_EX}

$$\   $$\            $$\                                       $$\             $$$$$$$$\                  $$\           
$$$\  $$ |           $$ |                                      $$ |            \__$$  __|                 $$ |          
$$$$\ $$ | $$$$$$\ $$$$$$\   $$\  $$\  $$\  $$$$$$\   $$$$$$\  $$ |  $$\          $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
$$ $$\$$ |$$  __$$\\_$$  _|  $$ | $$ | $$ |$$  __$$\ $$  __$$\ $$ | $$  |         $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
$$ \$$$$ |$$$$$$$$ | $$ |    $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$$$$$  /          $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
$$ |\$$$ |$$   ____| $$ |$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$  _$$<           $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
$$ | \$$ |\$$$$$$$\  \$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      $$ | \$$\          $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
\__|  \__| \_______|  \____/  \_____\____/  \______/ \__|      \__|  \__|         \__| \______/  \______/ \__|\_______/ 
                                                                                                                        
                                                                                                                        
                                                100 - Return To Main Menu                                                             
"""
    print(ascii)

def network_main():
    clear()
    Network_ascii()
    print("                                     [1] - Run IP Lookup")
    print("                                     [2] - Run IP Pinger")
    print("                                     [3] - Run Site Multitool")
    option = input("Option >> ")
    if option == '1':
        get_all_ips()
    elif option == '2':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        ip_lookup_download(run_option, Download_option=False)
    elif option == '3':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        ip_pinger_download(run_option, Download_option=False)
    elif option == '4':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        site_checker(run_option, Download_option=False)
    elif option == '100':
        main()
    else:
        print("Invalid...")
        time.sleep(0.5)
        network_main()

def discord_ascii():
    discord_ascii = f""" {Fore.MAGENTA}
    
 *******   **                                      **       **********                    **        
/**////** //                                      /**      /////**///                    /**        
/**    /** **  ******  *****   ******  ******     /**          /**      ******   ******  /**  ******
/**    /**/** **////  **///** **////**//**//*  ******          /**     **////** **////** /** **//// 
/**    /**/**//***** /**  // /**   /** /** /  **///**          /**    /**   /**/**   /** /**//***** 
/**    ** /** /////**/**   **/**   /** /**   /**  /**          /**    /**   /**/**   /** /** /////**
/*******  /** ****** //***** //****** /***   //******          /**    //****** //******  *** ****** 
///////   // //////   /////   //////  ///     //////           //      //////   //////  /// //////  
                                        b - Return to main menu"""
    print(discord_ascii)

def discord_tools_main():
    clear()
    discord_ascii()
    print("                        [1] - Run Webhook Multitool")
    print("                        [2] - Run Token Validator")
    print("                        [3] - Run Nitro Generator")
    print("                        [4] - Run Server Info Checker")
    option = input("Option >> ")
    if option == '1':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        webhook_mutltitool_download(run_option, Download_option=False)
    elif option == '2':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        token_validator(run_option, Download_option=False)
    elif option == '3':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        nitro_gen_download(run_option, return_to_menu=False)
    elif option == '4':
        run_option = input("You wanna run the tool? [Y or N] >> ")
        server_checker(run_option, return_to_menu=False)
    elif option.strip() == 'b':
        print("Taking you to main menu...")
        time.sleep(0.5)
        main()
    else:
        print("Invalid...")
        time.sleep(0.5)
        discord_tools_main()

if __name__ == '__main__':
    main()

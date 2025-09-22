import requests
import re
import os
from colorama import Fore


def the_ascii_art():
    ascii_art = f""" {Fore.LIGHTCYAN_EX}
___       __   __           ___  __                       _____               __    _______           __          
/ _ \___  / /  / /__ __ __  / _ \/ /  ___ ___ _____ ____  / ___/__  __ _____  / /_  / ___/ /  ___ ____/ /_____ ____
/ , _/ _ \/ _ \/ / _ \\ \ / / ___/ /__/ _ `/ // / -_) __/ / /__/ _ \/ // / _ \/ __/ / /__/ _ \/ -_) __/  '_/ -_) __/
/_/|_|\___/_.__/_/\___/_\_\ /_/  /____/\_,_/\_, /\__/_/    \___/\___/\_,_/_//_/\__/  \___/_//_/\__/\__/_/\_\\__/_/ 
                                           /___/                     
"""
    print(ascii_art)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class RobloxPlayerCountRecovery:
    def __init__(self):
        clear()
        the_ascii_art()
        try:
            self.universal_id_data = None
            self.universal_id = None
            self.place_id = None
            self.payload = None
            self.player_count = None
            self.items = None
            self.roblox_link = input(f"Enter roblox game browser link {Fore.LIGHTWHITE_EX}>>{Fore.LIGHTBLUE_EX} ")
            self.match = re.search(r'/games/(\d+)', str(self.roblox_link))
            self.get_roblox_place_id()
            self.universal_id_url = f"https://apis.roblox.com/universes/v1/places/{self.place_id}/universe"
            self.universal_id_response = requests.get(self.universal_id_url)
            self.get_roblox_universal_id()
            if not self.universal_id:
                input(f"universal id not found{Fore.LIGHTWHITE_EX}...{Fore.LIGHTBLUE_EX}")
            self.player_count_url = f"https://games.roblox.com/v1/games?universeIds={self.universal_id}"
            self.player_count_response = requests.get(self.player_count_url)
            self.get_roblox_player_count()
            if not self.player_count:
                input("Failed to Find Player Count...")
        except Exception as e:
            input(f"Error >> {e}")

    def get_roblox_place_id(self):
        if self.match:
            self.place_id = self.match.group(1)
            print(f"Phase 1 Complete{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX} Found place_id: {self.place_id}")
        else:
            print("Roblox Place ID not found in Link")

    def get_roblox_universal_id(self):
        if self.universal_id_response.status_code == 200:
            self.universal_id_data = self.universal_id_response.json()
            self.universal_id = self.universal_id_data["universeId"]
            print(f"Phase 2 Complete{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX} Found universal_id{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLUE_EX} {self.universal_id}")
        else:
            input(f"Invalid Status code >> {self.universal_id_response.status_code}")

    def get_roblox_player_count(self):
        if self.player_count_response.status_code == 200:
            self.payload = self.player_count_response.json()
            self.items = self.payload.get("data") or []
            self.player_count = self.items[0].get("playing") if self.items else None
            print(f"Phase 3 Complete: Found player_count")
            input(f"\n{self.player_count} Players Online :3...")
        else:
            input(f"Invalid Status Code >> {self.player_count_response.status_code}")

while True:
    RobloxPlayerCountRecovery()

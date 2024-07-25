import requests
import json
import urllib.parse
import time
import os
from colorama import Fore, Style, init

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_query_ids(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
        
def art():
    print("\033[1;91m" + r""" ______  _               _    
 | ___ \| |             | |   
 | |_/ /| |  __ _   ___ | | __
 | ___ \| | / _` | / __|| |/ /
 | |_/ /| || (_| || (__ |   < 
 \____/ |_| \__,_| \___||_|\_\
""" + "\033[0m" + "\033[1;92m" + r""" ______                                   
 |  _  \                                  
 | | | | _ __   __ _   __ _   ___   _ __  
 | | | || '__| / _` | / _` | / _ \ | '_ \ 
 | |/ / | |   | (_| || (_| || (_) || | | |
 |___/  |_|    \__,_| \__, | \___/ |_| |_|
                       __/ |              
                      |___/               
""" + "\033[0m" + "\033[1;93m" + r"""  _   _               _                
 | | | |             | |               
 | |_| |  __ _   ___ | | __  ___  _ __ 
 |  _  | / _` | / __|| |/ / / _ \| '__|
 | | | || (_| || (__ |   < |  __/| |   
 \_| |_/ \__,_| \___||_|\_\ \___||_| 
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Black Dragon Hacker\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/BlackDragonHacker007\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/BlackDragonHacker\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m--------------[Major Bot]--------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def decode_query_id(query_id):
    params = urllib.parse.parse_qs(query_id)
    user_info_encoded = params.get('user')[0]
    user_info_decoded = urllib.parse.unquote(user_info_encoded)
    user_info_json = json.loads(user_info_decoded)
    user_id = user_info_json.get('id')
    return user_id

def login(query_id):
    url_login = "https://major.glados.app/api/auth/tg/"
    payload = {"init_data": query_id}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_login, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Login failed with status code: {response.status_code}")
        return None

def get_user_rating(data):
    return data.get('user', {}).get('rating')

def get_access_token(data):
    return data.get('access_token')

def perform_daily_spin(access_token):
    url_spin = "https://major.glados.app/api/roulette"
    headers_spin = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_spin, headers=headers_spin)
    return response

def check_squad_status(user_id, access_token):
    url_check_squad = f"https://major.glados.app/api/users/{user_id}/"
    headers_check_squad = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.get(url_check_squad, headers=headers_check_squad)
    if response.status_code == 200:
        return response.json().get('squad_id')
    else:
        print(f"Failed to check squad status with status code: {response.status_code}")
        return None

def join_squad(access_token):
    squad_id = 2210217271
    url_join_squad = f"https://major.glados.app/api/squads/{squad_id}/join/"
    headers_join_squad = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_join_squad, headers=headers_join_squad)
    if response.status_code == 201:
        return True
    else:
        print(f"Failed to join squad with status code: {response.status_code}")
        return False

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')  # Clear the countdown message

def main():
    query_ids = read_query_ids('data.txt')
    art()
    while True:
        for index, query_id in enumerate(query_ids, start=1):
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{index}------")
            
            user_id = decode_query_id(query_id)
            login_data = login(query_id)
            
            if login_data:
                user_rating = get_user_rating(login_data)
                if user_rating is not None:
                    print(f"{Fore.YELLOW + Style.BRIGHT}Balance: {user_rating}")
                else:
                    print("User rating not found in response.")
                
                access_token = get_access_token(login_data)
                if access_token:
                    response_spin = perform_daily_spin(access_token)
                    if response_spin.status_code == 201:
                        spin_data = response_spin.json()
                        rating_award = spin_data.get("rating_award")
                        user_rating_after = spin_data.get("user_rating_after")
                        print(f"{Fore.GREEN + Style.BRIGHT}Claim Successful")
                        print(f"{Fore.MAGENTA + Style.BRIGHT}Daily Spin Reward: {rating_award}")
                        print(f"{Fore.CYAN + Style.BRIGHT}New Balance: {user_rating_after}")
                    elif response_spin.status_code == 400:
                        print(f"{Fore.RED + Style.BRIGHT}Daily Spin Already Claimed")

                    squad_id = check_squad_status(user_id, access_token)
                    if squad_id == 2210217271:
                        print(f"", end = "")
                    else:
                        if join_squad(access_token):
                            squad_id_after = check_squad_status(user_id, access_token)
                            if squad_id_after == 2210217271:
                                print(f"{Fore.GREEN + Style.BRIGHT}Squad Joined Successfully")
                            else:
                                print(f"{Fore.RED + Style.BRIGHT}Failed to join squad.")
                else:
                    print("Access token not found in login response.")
            else:
                print("Failed to retrieve login data.")
            print()  # Print a newline for better readability
        
        countdown_timer(5 * 60 * 60)
        clear_terminal()
        art()  # 5 hours in seconds

if __name__ == "__main__":
    main()

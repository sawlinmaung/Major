import requests
import json
import urllib.parse
import time
import random
import os
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_proxy(proxies):
    return random.choice(proxies) if proxies else None        

def read_query_ids(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def read_proxies(file_path):
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
    user_info_encoded = params.get('user', [''])[0]
    user_info_decoded = urllib.parse.unquote(user_info_encoded)
    user_info_json = json.loads(user_info_decoded)
    user_id = user_info_json.get('id')
    return user_id

def login(query_id, proxies=None):
    url_login = "https://major.glados.app/api/auth/tg/"
    payload = {"init_data": query_id}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_login, headers=headers, data=json.dumps(payload), proxies=proxies)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Login failed with status code: {response.status_code}")
        return None

def get_user_rating(data):
    return data.get('user', {}).get('rating')

def get_access_token(data):
    return data.get('access_token')

def perform_daily_spin(access_token, proxies=None):
    url_spin = "https://major.glados.app/api/roulette"
    headers_spin = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_spin, headers=headers_spin, proxies=proxies)
    return response

def perform_daily(access_token, proxies=None):
    url_daily = "https://major.glados.app/api/user-visits/visit/"
    headers_daily = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_daily, headers=headers_daily, proxies=proxies)
    return response

def check_squad_status(user_id, access_token, proxies=None):
    url_check_squad = f"https://major.glados.app/api/users/{user_id}/"
    headers_check_squad = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.get(url_check_squad, headers=headers_check_squad, proxies=proxies)
    if response.status_code == 200:
        return response.json().get('squad_id')
    else:
        print(f"Failed to check squad status with status code: {response.status_code}")
        return None

def join_squad(access_token, proxies=None):
    squad_id = 2210217271
    url_join_squad = f"https://major.glados.app/api/squads/{squad_id}/join/"
    headers_join_squad = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://major.glados.app/"
    }
    response = requests.post(url_join_squad, headers=headers_join_squad, proxies=proxies)
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

def check_proxy(proxy):
    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get("https://www.google.com", proxies=proxy_dict, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN + Style.BRIGHT}Proxy is Live: {proxy[:3]}.....{proxy[-3:]}")
            return proxy_dict
    except:
        print(f"{Fore.RED + Style.BRIGHT}Proxy is Dead: {proxy}")
    return None    

def get_working_proxy(proxies):
    while True:
        proxy = get_random_proxy(proxies)
        if proxy:
            live_proxy = check_proxy(proxy)
            if live_proxy:
                return live_proxy
        else:
            print(f"{Fore.RED + Style.BRIGHT}No proxies available. Exiting.")
            return None

def main():
    query_ids = read_query_ids('data.txt')
    clear_terminal()
    art()
    
    use_proxy = input("Do you want to use proxy? (y/n): ").strip().lower()
    if use_proxy == 'y':
        proxies = read_proxies('proxy.txt')
        if not proxies:
            print(f"{Fore.RED + Style.BRIGHT}No proxies found. Exiting.")
            return
    else:
        proxies = None

    while True:
        for index, query_id in enumerate(query_ids, start=1):
            print(f"{Fore.CYAN + Style.BRIGHT}------Account No.{index}------")
            
            user_id = decode_query_id(query_id)
            if user_id is None:
                print(f"{Fore.RED + Style.BRIGHT}Failed to decode user ID for account {index}. Skipping...")
                continue

            proxy_dict = None
            if proxies:
                proxy_dict = get_working_proxy(proxies)
                if not proxy_dict:
                    print(f"{Fore.RED + Style.BRIGHT}No working proxy found. Skipping account {index}.")
                    continue

            login_data = login(query_id, proxies=proxy_dict)
            if not login_data:
                print(f"{Fore.RED + Style.BRIGHT}Login failed for account {index}.")
                continue

            access_token = get_access_token(login_data)
            rating = get_user_rating(login_data)

            if rating is None:
                print(f"{Fore.RED + Style.BRIGHT}Failed to retrieve rating for account {index}.")
                continue

            print(f"{Fore.YELLOW + Style.BRIGHT}Balance: {rating}")

            if access_token:
                response_spin = perform_daily_spin(access_token, proxies=proxy_dict)
                if response_spin.status_code == 201:
                    spin_data = response_spin.json()
                    rating_award = spin_data.get("rating_award")
                    user_rating_after = spin_data.get("user_rating_after")
                    print(f"{Fore.GREEN + Style.BRIGHT}Claim Successful")
                    print(f"{Fore.MAGENTA + Style.BRIGHT}Daily Spin Reward: {rating_award}")
                    print(f"{Fore.CYAN + Style.BRIGHT}New Balance: {user_rating_after}")
                elif response_spin.status_code == 400:
                    print(f"{Fore.RED + Style.BRIGHT}Daily Spin Already Claimed")

                response_daily = perform_daily(access_token, proxies=proxy_dict)
                if response_daily.status_code == 200:
                    daily_data = response_daily.json()
                    if daily_data.get('is_increased'):
                        print(f"{Fore.GREEN + Style.BRIGHT}Daily Bonus Claimed Successfully")
                    else:
                        print(f"{Fore.RED + Style.BRIGHT}Daily Bonus Already Claimed")
                else:
                    print(f"{Fore.RED + Style.BRIGHT}Failed to perform daily task with status code: {response_daily.status_code}")

                squad_id = check_squad_status(user_id, access_token, proxies=proxy_dict)
                if squad_id == 2210217271:
                    print("", end = "")
                else:
                    if join_squad(access_token, proxies=proxy_dict):
                        squad_id_after = check_squad_status(user_id, access_token, proxies=proxy_dict)
                        if squad_id_after == 2210217271:
                            print(f"{Fore.GREEN + Style.BRIGHT}Squad Joined Successfully")
                        else:
                            print(f"{Fore.RED + Style.BRIGHT}Failed to join squad.")
            else:
                print(f"{Fore.RED + Style.BRIGHT}Access token not found in login response for account {index}.")

            print()  # Print a newline for better readability
        
        countdown_timer(12 * 60 * 60)  # 12 hours in seconds
        clear_terminal()
        art()  # Refresh the banner

if __name__ == "__main__":
    main()

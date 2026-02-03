import requests
import time
import random
import os

URL = "https://www.anthropic.com/news/claude-sonnet-5"

USER_AGENTS = [
    # Chrome Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    
    # Chrome Android
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    
    # Chrome iPhone (Chrome on iOS uses Safari engine but still valid UA)
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/133.0.0.0 Mobile/15E148 Safari/604.1",
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    try:
        response = requests.get(URL, headers=headers, timeout=10)

        if response.status_code == 404:
            print("Checked... no results.")
        elif response.status_code == 200:
            clear()
            print("\n" * 2)
            print("🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
            print("🔥🔥🔥  FINALLY SONNET 5 RELEASED!!! 🔥🔥🔥")
            print("🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
            print("\nGO CHECK IT NOW:", URL)
            break
        else:
            print(f"Checked... received status code {response.status_code}")

    except requests.RequestException as e:
        print("Error checking page:", e)

    time.sleep(random.randint(5, 10))

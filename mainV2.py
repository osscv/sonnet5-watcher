import requests
import time
import random
import os
import re

URLS = {
    "news": "https://www.anthropic.com/news/claude-sonnet-5",
    "docs": "https://platform.claude.com/docs/en/about-claude/models/overview"
}

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

# Pattern to match Claude Sonnet 5 model strings
SONNET_5_PATTERN = re.compile(r'claude-sonnet-5(?:-thinking)?-\d{8}', re.IGNORECASE)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_url(url, headers):
    """Check a URL for Sonnet 5 release indicators"""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            return False, "404"
        elif response.status_code == 200:
            # Check if this is the news page or docs page
            if "news/claude-sonnet-5" in url:
                return True, "news_page_exists"
            else:
                # For docs page, check content for Sonnet 5 model strings
                if SONNET_5_PATTERN.search(response.text):
                    matches = SONNET_5_PATTERN.findall(response.text)
                    return True, f"found_models: {', '.join(set(matches))}"
                return False, "200_no_match"
        else:
            return False, f"status_{response.status_code}"
            
    except requests.RequestException as e:
        return False, f"error: {str(e)[:50]}"

while True:
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    found = False
    results = {}
    
    for name, url in URLS.items():
        is_found, status = check_url(url, headers)
        results[name] = status
        if is_found:
            found = True
    
    if found:
        clear()
        print("\n" * 2)
        print("🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
        print("🔥🔥🔥  FINALLY SONNET 5 RELEASED!!! 🔥🔥🔥")
        print("🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨")
        print("\nDetection details:")
        for name, status in results.items():
            print(f"  {name}: {status}")
        print("\nURLs to check:")
        for name, url in URLS.items():
            print(f"  {name}: {url}")
        break
    else:
        print(f"Checked... News: {results['news']}, Docs: {results['docs']}")

    time.sleep(random.randint(5, 10))

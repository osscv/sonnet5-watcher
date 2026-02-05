import requests
import time
import random
import os
import re

URLS = {
    "news_sonnet5": "https://www.anthropic.com/news/claude-sonnet-5",
    "news_claude5": "https://www.anthropic.com/news/claude-5",
    "docs": "https://docs.anthropic.com/en/docs/about-claude/models"
}

USER_AGENTS = [
    # Chrome Desktop
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    
    # Chrome Android
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Samsung Galaxy S23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    
    # Chrome iPhone
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/133.0.0.0 Mobile/15E148 Safari/604.1",
]

# Patterns to match Claude 5 model strings (multiple variations)
CLAUDE_5_PATTERNS = [
    re.compile(r'claude-5(?:-sonnet|-opus|-haiku)?(?:-thinking)?-\d{8}', re.IGNORECASE),
    re.compile(r'claude-sonnet-5(?:-thinking)?-\d{8}', re.IGNORECASE),
    re.compile(r'claude-opus-5(?:-thinking)?-\d{8}', re.IGNORECASE),
    re.compile(r'claude-haiku-5(?:-thinking)?-\d{8}', re.IGNORECASE),
]

# Keywords that might indicate Claude 5 announcement
ANNOUNCEMENT_KEYWORDS = [
    "claude 5",
    "claude-5",
    "sonnet 5",
    "opus 5",
    "haiku 5",
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_url(url, headers):
    """Check a URL for Claude 5 release indicators"""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            return False, "404"
        elif response.status_code == 200:
            # Check if this is a news page
            if "/news/claude" in url:
                # News page exists = announcement likely made
                return True, "news_page_exists"
            else:
                # For docs page, check content for Claude 5 model strings
                text = response.text.lower()
                
                # Check for model string patterns
                found_models = set()
                for pattern in CLAUDE_5_PATTERNS:
                    matches = pattern.findall(response.text)
                    found_models.update(matches)
                
                if found_models:
                    return True, f"found_models: {', '.join(found_models)}"
                
                # Check for announcement keywords
                for keyword in ANNOUNCEMENT_KEYWORDS:
                    if keyword in text:
                        return True, f"found_keyword: {keyword}"
                
                return False, "200_no_match"
        else:
            return False, f"status_{response.status_code}"
            
    except requests.RequestException as e:
        return False, f"error: {str(e)[:50]}"

def main():
    check_count = 0
    
    while True:
        check_count += 1
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
            print("🚨" * 16)
            print("🔥🔥🔥  CLAUDE 5 DETECTED!!! 🔥🔥🔥")
            print("🚨" * 16)
            print(f"\nFound after {check_count} checks")
            print("\nDetection details:")
            for name, status in results.items():
                indicator = "✅" if "404" not in status and "no_match" not in status else "❌"
                print(f"  {indicator} {name}: {status}")
            print("\nURLs to check:")
            for name, url in URLS.items():
                print(f"  • {url}")
            print("\n" + "🎉" * 16)
            break
        else:
            # Create compact status line
            status_line = f"[Check #{check_count}] "
            status_parts = []
            for name, status in results.items():
                short_name = name.replace("news_", "").replace("_", "-")
                status_parts.append(f"{short_name}: {status}")
            status_line += " | ".join(status_parts)
            
            print(status_line)

        # Random delay between checks (5-10 seconds)
        time.sleep(random.randint(5, 10))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")

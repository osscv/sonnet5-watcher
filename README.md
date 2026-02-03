# 🚨 sonnet5-watcher

A simple Python watcher that checks whether **Claude Sonnet 5** has been officially released.

## 🧠 Idea

Sonnet 4.5 was announced at:

👉 https://www.anthropic.com/news/claude-sonnet-4-5  

From this pattern, it is reasonable to predict that the Sonnet 5 announcement page will be:

👉 https://www.anthropic.com/news/claude-sonnet-5  

This tool continuously monitors the page and alerts you the moment it goes live.

No more manual refreshing. No more F5 spam 🙂

---

## ⚙️ Features

✅ Checks the page every **5–10 seconds**  
✅ Uses **random Chrome User-Agent** (desktop + mobile)  
✅ Lightweight and fast  
✅ Clear console alerts  
✅ Stops automatically once the page is available  

---

## 📦 Requirements

- Python 3.8+
- `requests`

Install dependency:

```bash
pip install requests

# 🚨 sonnet5-watcher

A simple Python watcher that checks whether **Claude Sonnet 5** has been officially released.

---

## 🧠 Idea

Sonnet 4.5 was announced at:

👉 https://www.anthropic.com/news/claude-sonnet-4-5  

From this pattern, it is reasonable to predict that the Sonnet 5 announcement page will be:

👉 https://www.anthropic.com/news/claude-sonnet-5  

Additionally, the Claude platform model overview may contain early mentions of Sonnet 5 under names like:

- `claude-sonnet-5-2026xxxx`  
- `claude-sonnet-5-thinking`  
- Other variations  

Check the overview here:

👉 https://platform.claude.com/docs/en/about-claude/models/overview  

This watcher monitors both pages and alerts you the moment any reference to Sonnet 5 appears.

No more manual refreshing. No more F5 spam 🙂

---

## ⚙️ Features

✅ Checks the **news page** every 5–10 seconds  
✅ Checks the **Claude models overview page** for keywords like `claude-sonnet-5-*`  
✅ Uses **random Chrome User-Agent** (desktop + mobile)  
✅ Lightweight and fast  
✅ Clear console alerts  
✅ Stops automatically once the page or reference is found  

---

## 📦 Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4` (for parsing the overview page)

Install dependencies:

```bash
pip install requests beautifulsoup4✅ Lightweight and fast  
✅ Clear console alerts  
✅ Stops automatically once the page is available  

---

## 📦 Requirements

- Python 3.8+
- `requests`

Install dependency:

```bash
pip install requests

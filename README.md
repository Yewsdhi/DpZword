# 🤖 Bio Mute Bot

A simple Telegram bot that **mutes new users if their bio contains suspicious links**.

## 🚀 Features
- Auto-mutes new members with `http` or `t.me` in their bio.
- Helps protect groups from spam/scam bots.
- Simple deployment to **Heroku**.

## ⚙️ Setup (Local)
1. Install requirements:
   ```bash
   pip install -r requirements.txt
# 🤖 Bio Mute Bot

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yourusername/bio-mute-bot)

heroku ps:scale worker=1

git init
git add .
git commit -m "Initial commit"
git push heroku main

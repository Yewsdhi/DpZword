import os

API_ID = int(os.getenv("API_ID", 12345))  # set in Heroku
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

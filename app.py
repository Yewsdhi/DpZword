{
  "name": "Boi Mute Link Bot",
  "description": "A Telegram bot that automatically mutes users who send links in groups.",
  "repository": "https://github.com/yourusername/BoiMuteLinkBot",
  "keywords": ["telegram", "pyrogram", "mute", "bot"],
  "env": {
    "API_ID": {
      "description": "Your Telegram API ID (from https://my.telegram.org)",
      "required": true
    },
    "API_HASH": {
      "description": "Your Telegram API Hash (from https://my.telegram.org)",
      "required": true
    },
    "BOT_TOKEN": {
      "description": "Your Bot Token (from @BotFather)",
      "required": true
    }
  },
  "formation": {
    "worker": {
      "quantity": 1,
      "size": "free"
    }
  },
  "stack": "heroku-22"
}

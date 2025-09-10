from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
import re, time, os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("BoiMuteLinkBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Regex for detecting links
link_regex = re.compile(r"(http[s]?://|t\.me/|www\.)")

@app.on_message(filters.group & filters.text)
async def mute_links(client, message):
    if message.from_user and link_regex.search(message.text):
        try:
            await message.chat.restrict_member(
                message.from_user.id,
                ChatPermissions(),  # no permission
                until_date=int(time.time()) + 3600  # mute 1 hour
            )
            await message.reply_text(
                f"🔇 {message.from_user.mention} ko 1 ghante ke liye mute kar diya gaya (link bhejne par)."
            )
        except Exception as e:
            print(e)

print("🤖 Boi Mute Link Bot started...")
app.run()

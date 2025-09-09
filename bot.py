import logging
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from config import API_ID, API_HASH, BOT_TOKEN

logging.basicConfig(level=logging.INFO)

app = Client(
    "bio_mute_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.new_chat_members)
async def check_bio(_, message):
    for member in message.new_chat_members:
        bio = (await app.get_users(member.id)).bio or ""
        if "http" in bio or "t.me" in bio:  # detect links in bio
            try:
                await message.chat.restrict_member(
                    member.id,
                    ChatPermissions(),  # mute user (no permissions)
                )
                await message.reply_text(
                    f"🔇 {member.mention} has been muted due to suspicious bio (link detected)."
                )
            except Exception as e:
                print(f"Error: {e}")

print("🤖 Bio Mute Bot Started...")
app.run()

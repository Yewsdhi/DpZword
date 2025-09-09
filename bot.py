import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ------------------------------
# Quotes Collection (Add More!)
# ------------------------------
DPZ_QUOTES = [
    "Sometimes silence speaks louder than words.",
    "Attitude is my middle name 😎",
    "Love is not about possession, it's about appreciation ❤️",
    "Hurt me with the truth, but never comfort me with a lie.",
    "A strong soul shines after every storm.",
    "I may be sad, but I will never be weak.",
    "Smile in front, pain behind the mask.",
    "Dream big, work hard, stay humble."
]

# ------------------------------
# Command Handlers
# ------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! I’m your DPZ Quotes Bot.\n\n"
        "Use /dpz to get a random DPZ quote."
    )

async def dpz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quote = random.choice(DPZ_QUOTES)
    await update.message.reply_text(f"✨ {quote}")

# ------------------------------
# Main Function
# ------------------------------
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ Error: BOT_TOKEN is missing! Please set it as environment variable.")
        return

    app = Application.builder().token(token).build()

    # Add commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dpz", dpz))

    # Run bot
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

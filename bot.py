import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Quotes database
quotes = {
    "love": [
        "You are my today and all of my tomorrows ❤️",
        "Love is friendship set on fire 🔥",
        "With you, every moment is sweet 🍯",
        "Love is not what you say, love is what you do 💕",
        "When I see you, my heart skips a beat 💓",
        "Every love story is beautiful, but ours is my favorite 💖",
        "I fell in love with the way you touched my soul 🌹"
    ],
    "sad": [
        "Tears come from the heart and not from the brain 💔",
        "It’s hard to forget someone who gave you so much to remember 💭",
        "Sometimes, the person you love the most hurts you the most 😔",
        "I’m not okay, but it’s okay 😞",
        "Behind my smile is a hurting heart 💔"
    ],
    "attitude": [
        "My life, my rules, my attitude 🛑",
        "I may not be perfect, but I’m always me 🔥",
        "Born to express, not to impress 💯",
        "Silent but dangerous ⚡",
        "Be yourself; everyone else is already taken 🙌"
    ]
}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to DPZ Words Bot ✨\n"
        "Use /dpz <category> to get a quote.\n"
        "Categories: love, sad, attitude"
    )

# DPZ command
async def dpz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /dpz <love|sad|attitude>")
        return

    category = context.args[0].lower()
    if category in quotes:
        quote = random.choice(quotes[category])
        await update.message.reply_text(quote)
    else:
        await update.message.reply_text("Category not found! Use: love, sad, attitude")

def main():
    token = os.getenv("BOT_TOKEN")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dpz", dpz))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

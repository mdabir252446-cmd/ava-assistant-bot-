
import os
import threading
from flask import Flask
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

APP_URL = "https://mdabir252446-cmd.github.io/ava-assistant-bot-/"

app = Flask(__name__)

@app.route("/")
def home():
    return "Ava Assistant is running!"

def run_bot():
    bot.infinity_polling(none_stop=True)

@bot.message_handler(commands=["start"])
def start_handler(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            "🚀 Open AVA App",
            web_app=WebAppInfo(url=APP_URL)
        )
    )
    bot.send_message(
        message.chat.id,
        "স্বাগতম Ava Assistant-এ!\n\n• ১২ ঘণ্টায় 100 AVA ক্লেইম করুন\n• রেট: 100 AVA = $0.01\n\nঅ্যাপ খুলতে নিচের বাটনে চাপ দিন:",
        reply_markup=markup
    )

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

import os
import threading
from flask import Flask
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

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
        InlineKeyboardButton("📋 Tasks", callback_data="tasks"),
        InlineKeyboardButton("👥 Friends", callback_data="friends"),
        InlineKeyboardButton("👤 Profile", callback_data="profile"),
    )
    bot.send_message(
        message.chat.id,
        "স্বাগতম Ava Assistant-এ! নিচের মেনু থেকে আপনার অপশন বেছে নিন:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "tasks":
        bot.answer_callback_query(call.id, "Tasks সেকশন আসছে")
        bot.send_message(call.message.chat.id, "📋 সহজ কাজগুলো (Tasks) এখানে যুক্ত করা হবে।")
    elif call.data == "friends":
        bot.answer_callback_query(call.id, "Friends সেকশন আসছে")
        bot.send_message(call.message.chat.id, "👥 রেফারেল ও ফ্রেন্ডস সিস্টেম এখানে থাকবে।")
    elif call.data == "profile":
        bot.answer_callback_query(call.id, "Profile সেকশন আসছে")
        bot.send_message(call.message.chat.id, "👤 আপনার প্রোফাইল ও ব্যালেন্স তথ্য এখানে দেখা যাবে।")

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

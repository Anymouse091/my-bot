import os
from threading import Thread
import telebot
from flask import Flask

BOT_TOKEN = "8668608150:AAFX2Ktk31CUbSWY60ap1jAIqE7EN0ZtAcY"
bot = telebot.TeleBot(BOT_TOKEN)

# 1. Render က Web Service တစ်ခုအနေနဲ့ သိစေရန် Flask ဝန်ဆောင်မှု ထည့်ခြင်း
app = Flask("")


@app.route("/")
def home():
    return "Telegram Bot is alive!"


def run_web():
    # Render သတ်မှတ်ပေးသော Port (သို့မဟုတ် Default 10000) ဖြင့် Run ခြင်း
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()


# 2. Telegram Bot Handlers
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ! Render ဆာဗာမှ Telegram Bot အလုပ်လုပ်နေပါပြီ။")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(
        message,
        f"ရရှိသော စာ: {message.text}\n(Render Bot အလုပ်လုပ်နေပါပြီ!)",
    )


if __name__ == "__main__":
    # Web server ကို Background မှာ အရင် Run မည်
    keep_alive()
    print("Telegram Bot စတင်နေပါပြီ...")
    # Telegram Bot ကို Polling စတင်မည်
    bot.infinity_polling()

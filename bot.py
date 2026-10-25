import os
import telebot

# BotFather က ရထားတဲ့ ကိုယ့်ရဲ့ Token အမှန်ကို ထည့်ပါ
BOT_TOKEN = "8668608150:AAFX2Ktk31CUbSWY60ap1jAIqE7EN0ZtAcY"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "မင်္ဂလာပါ! Render ဆာဗာမှ Telegram Bot အလုပ်လုပ်နေပါပြီ။")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"ရရှိသော စာ: {message.text}\n(Bot အလုပ်လုပ်နေပါပြီ!)")

if __name__ == "__main__":
    print("Bot စတင်နေပါပြီ...")
    bot.infinity_polling()

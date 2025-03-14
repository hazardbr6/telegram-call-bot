import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from spoof import spoof_number
from vpn import change_ip
from call_handler import make_call

# Telegram Bot Token and Group ID (hardcoded for now; consider using environment variables)
BOT_TOKEN = "7871650691:AAHArQ17NVAZcNwDF0ZAthi7_yrsrd1mRyY"
GROUP_ID = "-4641030948"

bot = telebot.TeleBot(BOT_TOKEN)
target_number = ""

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "📞 Enter the phone number to dial:")
    bot.register_next_step_handler(message, handle_number)

def handle_number(message):
    global target_number
    target_number = message.text.strip()
    markup = InlineKeyboardMarkup()
    codes = {"+92": "🇵🇰 Pakistan", "+1": "🇺🇸 USA", "+7": "🇷🇺 Russia", "+972": "🇮🇱 Israel"}
    for code, name in codes.items():
        markup.add(InlineKeyboardButton(name, callback_data=code))
    bot.send_message(message.chat.id, "📌 Select a country code for spoofing:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("+"))
def handle_spoof(call):
    # Generate spoofed caller ID using the selected country code and the target number
    spoofed = spoof_number(call.data, target_number)
    bot.send_message(call.message.chat.id, f"✅ Spoofed Caller ID: {spoofed}")
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📞 Call", callback_data="call"))
    bot.send_message(call.message.chat.id, "🔹 Click 'Call' to start dialing.", reply_markup=markup)
    # Store spoofed number for later use (if needed)
    call.data = spoofed

@bot.callback_query_handler(func=lambda call: call.data == "call")
def handle_call(call):
    bot.send_message(call.message.chat.id, "🔄 Changing IP for security...")
    change_ip()
    success, result_msg = make_call(target_number)
    if success:
        bot.send_message(call.message.chat.id, f"📡 Call in progress using {result_msg}")
    else:
        bot.send_message(call.message.chat.id, f"❌ Call failed: {result_msg}")

if __name__ == "__main__":
    bot.polling()

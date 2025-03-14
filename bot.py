import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from spoof import spoof_number
from vpn import change_ip
from call_handler import make_call

# Telegram Bot Token
BOT_TOKEN = "7871650691:AAHArQ17NVAZcNwDF0ZAthi7_yrsrd1mRyY"
GROUP_ID = "-4641030948"

bot = telebot.TeleBot(BOT_TOKEN)

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "📞 Enter the number to dial:")
    bot.register_next_step_handler(message, ask_spoof_code)

# Ask for country code spoofing
def ask_spoof_code(message):
    global target_number
    target_number = message.text.strip()

    markup = InlineKeyboardMarkup()
    codes = {"+92": "🇵🇰 Pakistan", "+1": "🇺🇸 USA", "+7": "🇷🇺 Russia", "+972": "🇮🇱 Israel"}
    for code, name in codes.items():
        markup.add(InlineKeyboardButton(name, callback_data=code))
    
    bot.send_message(message.chat.id, "📌 Select a country code for spoofing:", reply_markup=markup)

# Handle country code selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("+"))
def spoof_selected(call):
    spoofed_number = spoof_number(call.data, target_number)
    bot.send_message(call.message.chat.id, f"✅ Spoofed Caller ID: {spoofed_number}")
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📞 Call", callback_data="call"))
    
    bot.send_message(call.message.chat.id, "🔹 Click 'Call' to start dialing.", reply_markup=markup)

# Handle call request
@bot.callback_query_handler(func=lambda call: call.data == "call")
def process_call(call):
    bot.send_message(call.message.chat.id, "🔄 Changing IP for security...")
    change_ip()

    success, message = make_call(target_number)

    if success:
        bot.send_message(call.message.chat.id, "📡 Connecting to voice chat...")
        # Logic for streaming audio (to be implemented)
    else:
        bot.send_message(call.message.chat.id, f"❌ Call failed: {message}")

# Run Bot
bot.polling()

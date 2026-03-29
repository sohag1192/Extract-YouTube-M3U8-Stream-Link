import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
BOT_TOKEN = '8425711356:AAHex14zhojqhuTs1rYx-coT8YiXPfHOYqk0'
ADMIN_ID = -52614771400  # Group/Channel ID
SERVER_LINK = 'http://100.100.100.6/'
TV_SERVER_LINK = 'http://100.100.100.2'
ICC_FTP_LINK = 'http://10.16.100.244/'

bot = telebot.TeleBot(BOT_TOKEN)

# ==========================================
# 🚀 /start & /help COMMAND (Menu & Links)
# ==========================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    server_btn = InlineKeyboardButton("🌐 SN Movies Server", url=SERVER_LINK)
    tv_server_btn = InlineKeyboardButton("📺 SN TV Server", url=TV_SERVER_LINK)
    icc_ftp_btn = InlineKeyboardButton("⚡ ICC FTP (PARTNER)", url=ICC_FTP_LINK)
    
    markup.add(server_btn)
    markup.add(tv_server_btn)
    markup.add(icc_ftp_btn)

    welcome_text = (
        "👋 **Welcome to the SN EMBY & ICC FTP Bot!**\n\n"
        "I am here to help you access the servers and request new content.\n\n"
        "🛠️ **Command Menu:**\n"
        "• `/request_movie [Name]` - Request a Movie\n"
        "• `/request_tv [Name]` - Request a TV Show\n"
        "• `/request_game [Name]` - Request a PC/Console Game\n"
        "• `/request_others [Name]` - Request Software/Music/Misc\n"
        "• `/help` - Show this menu again\n\n"
        "👇 **Click the buttons below to access the servers:**"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# ==========================================
# 🍿 /request_movie COMMAND
# ==========================================
@bot.message_handler(commands=['request_movie'])
def handle_movie_request(message):
    request_text = message.text.replace('/request_movie', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include the movie name!\n\n*Format:* `/request_movie Movie Name`", parse_mode='Markdown')
        return

    username = f"(@{message.from_user.username})" if message.from_user.username else ""
    
    admin_msg = (
        "🚨 **NEW CONTENT REQUEST** 🚨\n\n"
        f"👤 **From:** {message.from_user.first_name} {username}\n"
        f"🆔 **User ID:** `{message.from_user.id}`\n"
        f"🎬 **Movie:** `{request_text}`" 
    )
    
    try:
        bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
        bot.reply_to(message, f"✅ Request for movie **{request_text}** sent to admin!", parse_mode='Markdown')
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "❌ Error: Could not send request. Admin might need to add the bot to the group.")

# ==========================================
# 📺 /request_tv COMMAND
# ==========================================
@bot.message_handler(commands=['request_tv'])
def handle_tv_request(message):
    request_text = message.text.replace('/request_tv', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include the TV show name!\n\n*Format:* `/request_tv Show Name`", parse_mode='Markdown')
        return

    username = f"(@{message.from_user.username})" if message.from_user.username else ""
    
    admin_msg = (
        "🚨 **NEW CONTENT REQUEST** 🚨\n\n"
        f"👤 **From:** {message.from_user.first_name} {username}\n"
        f"🆔 **User ID:** `{message.from_user.id}`\n"
        f"🎞️ **TV Show:** `{request_text}`" 
    )
    
    try:
        bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
        bot.reply_to(message, f"✅ Request for TV show **{request_text}** sent to admin!", parse_mode='Markdown')
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "❌ Error: Could not send request.")

# ==========================================
# 🎮 /request_game COMMAND
# ==========================================
@bot.message_handler(commands=['request_game'])
def handle_game_request(message):
    request_text = message.text.replace('/request_game', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include the game name!\n\n*Format:* `/request_game Game Name`", parse_mode='Markdown')
        return

    username = f"(@{message.from_user.username})" if message.from_user.username else ""

    admin_msg = (
        "🚨 **NEW CONTENT REQUEST** 🚨\n\n"
        f"👤 **From:** {message.from_user.first_name} {username}\n"
        f"🆔 **User ID:** `{message.from_user.id}`\n"
        f"🕹️ **Game:** `{request_text}`" 
    )
    
    try:
        bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
        bot.reply_to(message, f"✅ Request for game **{request_text}** sent to admin!", parse_mode='Markdown')
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "❌ Error: Could not send request.")

# ==========================================
# 📦 /request_others COMMAND
# ==========================================
@bot.message_handler(commands=['request_others'])
def handle_others_request(message):
    request_text = message.text.replace('/request_others', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include what you are looking for!\n\n*Format:* `/request_others Software/Music/Item Name`", parse_mode='Markdown')
        return

    username = f"(@{message.from_user.username})" if message.from_user.username else ""

    admin_msg = (
        "🚨 **NEW CONTENT REQUEST** 🚨\n\n"
        f"👤 **From:** {message.from_user.first_name} {username}\n"
        f"🆔 **User ID:** `{message.from_user.id}`\n"
        f"📦 **Misc Item:** `{request_text}`" 
    )
    
    try:
        bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
        bot.reply_to(message, f"✅ Request for **{request_text}** sent to admin!", parse_mode='Markdown')
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "❌ Error: Could not send request.")

# ==========================================
# 🤖 AUTO-REPLY (Catch-all for regular text)
# ==========================================
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    reply_text = (
        "🤖 I am an automated bot.\n\n"
        "Type `/help` or `/start` to see the server links and the list of request commands."
    )
    bot.reply_to(message, reply_text, parse_mode='Markdown')

# ==========================================
# 🏃‍♂️ RUN THE BOT
# ==========================================
print("Bot is running...")
bot.infinity_polling()
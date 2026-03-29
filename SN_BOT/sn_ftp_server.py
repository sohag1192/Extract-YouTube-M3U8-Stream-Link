import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# ⚠️ Friendly reminder: Keep your BOT_TOKEN secret! 
BOT_TOKEN = '8425711356:SS-coT8YiXPfHOYqk'
ADMIN_ID = 8409643894 
SERVER_LINK = 'http://100.100.100.6/'
TV_SERVER_LINK = 'http://100.100.100.2'
ICC_FTP_LINK = 'http://10.16.100.244/' # NEW ICC FTP Link

bot = telebot.TeleBot(BOT_TOKEN)

# ==========================================
# 🚀 /start & /help COMMAND (Menu & Links)
# ==========================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Create the Inline Buttons
    markup = InlineKeyboardMarkup()
    server_btn = InlineKeyboardButton("🌐 Movies Server", url=SERVER_LINK)
    tv_server_btn = InlineKeyboardButton("📺 TV Server", url=TV_SERVER_LINK)
    icc_ftp_btn = InlineKeyboardButton("⚡ ICC FTP Server", url=ICC_FTP_LINK)
    
    # Add buttons (stacking them vertically for a clean look)
    markup.add(server_btn)
    markup.add(tv_server_btn)
    markup.add(icc_ftp_btn)

    # Welcome & Help Text
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

    admin_msg = f"🎬 **NEW MOVIE REQUEST** 🎬\n\n👤 **From:** {message.from_user.first_name}\n🆔 **ID:** `{message.from_user.id}`\n🎥 **Movie:** {request_text}"
    bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
    bot.reply_to(message, f"✅ Request for movie **{request_text}** sent to admin!", parse_mode='Markdown')

# ==========================================
# 📺 /request_tv COMMAND
# ==========================================
@bot.message_handler(commands=['request_tv'])
def handle_tv_request(message):
    request_text = message.text.replace('/request_tv', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include the TV show name!\n\n*Format:* `/request_tv Show Name`", parse_mode='Markdown')
        return

    admin_msg = f"📺 **NEW TV SHOW REQUEST** 📺\n\n👤 **From:** {message.from_user.first_name}\n🆔 **ID:** `{message.from_user.id}`\n🎞️ **Show:** {request_text}"
    bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
    bot.reply_to(message, f"✅ Request for TV show **{request_text}** sent to admin!", parse_mode='Markdown')

# ==========================================
# 🎮 /request_game COMMAND
# ==========================================
@bot.message_handler(commands=['request_game'])
def handle_game_request(message):
    request_text = message.text.replace('/request_game', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include the game name!\n\n*Format:* `/request_game Game Name`", parse_mode='Markdown')
        return

    admin_msg = f"🎮 **NEW GAME REQUEST** 🎮\n\n👤 **From:** {message.from_user.first_name}\n🆔 **ID:** `{message.from_user.id}`\n🕹️ **Game:** {request_text}"
    bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
    bot.reply_to(message, f"✅ Request for game **{request_text}** sent to admin!", parse_mode='Markdown')

# ==========================================
# 📦 /request_others COMMAND
# ==========================================
@bot.message_handler(commands=['request_others'])
def handle_others_request(message):
    request_text = message.text.replace('/request_others', '').strip()
    if not request_text:
        bot.reply_to(message, "⚠️ Please include what you are looking for!\n\n*Format:* `/request_others Software/Music/Item Name`", parse_mode='Markdown')
        return

    admin_msg = f"📦 **NEW MISC REQUEST** 📦\n\n👤 **From:** {message.from_user.first_name}\n🆔 **ID:** `{message.from_user.id}`\n🔎 **Item:** {request_text}"
    bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
    bot.reply_to(message, f"✅ Request for **{request_text}** sent to admin!", parse_mode='Markdown')

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
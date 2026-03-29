import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
BOT_TOKEN = 'YOUR BOY'
ADMIN_ID = 8409643894 # Kept as an integer
SERVER_LINK = 'http://100.100.100.6/'
TV_SERVER_LINK = 'http://100.100.100.2'

bot = telebot.TeleBot(BOT_TOKEN)

# ==========================================
# 🚀 /start COMMAND (Welcome Text & Buttons)
# ==========================================
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Create the Inline Buttons
    markup = InlineKeyboardMarkup()
    server_btn = InlineKeyboardButton("🌐 Go to Movies Server", url=SERVER_LINK)
    tv_server_btn = InlineKeyboardButton("📺 Go to TV Server", url=TV_SERVER_LINK)
    
    # Add buttons (stacking them vertically)
    markup.add(server_btn)
    markup.add(tv_server_btn)

    # Welcome Text
    welcome_text = (
        "👋 Welcome to the **SN EMBY FTP SERVER** Bot!\n\n"
        "I am here to help you connect to the servers and manage movie/TV requests.\n\n"
        "🎬 **How to request a movie or show:**\n"
        "Just type: `/request [Title Name]`\n"
        "*(Example: /request The Matrix)*\n\n"
        "Click the buttons below to access the servers directly:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# ==========================================
# 📥 /request COMMAND (Send to Admin)
# ==========================================
@bot.message_handler(commands=['request'])
def handle_request(message):
    # Extract the requested title from the user's message
    request_text = message.text.replace('/request', '').strip()

    # If they just typed /request without a title
    if not request_text:
        bot.reply_to(message, "⚠️ Please include the movie or show name!\n\n*Format:* `/request Title Name`", parse_mode='Markdown')
        return

    # Format the message to send to the Admin
    username = f"@{message.from_user.username}" if message.from_user.username else "No Username"
    admin_msg = (
        "🚨 **NEW CONTENT REQUEST** 🚨\n\n"
        f"👤 **From:** {message.from_user.first_name} ({username})\n"
        f"🆔 **User ID:** `{message.from_user.id}`\n"
        f"🎥 **Request:** {request_text}"
    )

    try:
        # Send to Admin
        bot.send_message(ADMIN_ID, admin_msg, parse_mode='Markdown')
        # Confirm to User
        bot.reply_to(message, f"✅ Your request for **{request_text}** has been successfully sent to the admin!", parse_mode='Markdown')
    except Exception as e:
        print(f"Error sending message to admin: {e}")
        bot.reply_to(message, "❌ Sorry, there was an error sending your request. The admin might need to start the bot first.")

# ==========================================
# 🤖 AUTO-REPLY (Catch-all for regular text)
# ==========================================
@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    # If the user types anything that isn't a command, auto-reply with instructions
    reply_text = (
        "🤖 I am an automated bot for the SN EMBY FTP SERVER.\n\n"
        "• To see the server links, type `/start`\n"
        "• To request content, type `/request [Title Name]`"
    )
    bot.reply_to(message, reply_text, parse_mode='Markdown')

# ==========================================
# 🏃‍♂️ RUN THE BOT
# ==========================================
print("Bot is running...")
bot.infinity_polling()
import telebot

# 1. Paste the API token you got from @BotFather
API_TOKEN = '8296157365:ss'
bot = telebot.TeleBot(API_TOKEN)

# 2. Define your bilingual announcement message
# Using triple quotes (""") allows for easy multi-line text
UPDATE_MESSAGE = """📢 **আপডেট:**
SN TV সেবা বর্তমানে আপনার ইন্টারনেট সংযোগে উপলব্ধ নয়।
সেবা চালু করতে অনুগ্রহ করে আপনার ইন্টারনেট সেবা প্রদানকারীর সাথে যোগাযোগ করুন।
আপনাদের অসুবিধার জন্য আমরা আন্তরিকভাবে দুঃখিত।

📢 **Update:**
SN TV service is currently not available on your internet connection.
To enable access, please contact your internet service provider.
We sincerely apologize for the inconvenience."""

# 3. Handle specific commands like /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_update_on_command(message):
    # Sends the message formatted with Markdown (for the bolding)
    bot.reply_to(message, UPDATE_MESSAGE, parse_mode='Markdown')

# 4. Auto-reply for ANY other text message a user sends
@bot.message_handler(func=lambda message: True)
def auto_reply_all(message):
    bot.reply_to(message, UPDATE_MESSAGE, parse_mode='Markdown')

# Starts the bot
print("🤖 SN TV Auto-reply Bot is running...")
bot.infinity_polling()
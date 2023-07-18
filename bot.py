from telegram import Update
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    message = "Hello! I'm your Telegram bot. How can I assist you?"
    bot.send_message(chat_id=chat_id, text=message)

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final

from googlesearch import search

"""


def main():
    updater = Updater(token="YOUR_API_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start_command)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()




"""
token: Final = "6061354792:AAF7UHyG5gboTAKVU8aX8Vw9W9xUu1Bikaw"

bot_username: Final = "@ioan_bot_bot"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! What book do you want me to tell you about?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a nice geeky bot. TEll me something to start the conversation")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Charles Dickens was a brit from the 19th century")



def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hi"
    elif "morometii" in processed:
        return "Este scris de Marin Preda"
    elif "moara cu noroc" in processed:
        return "ioan slavici"
    else:
        try:
            search_results = list(search(text, num=1, stop=1, pause=2))
            if search_results:
                return f"Here is the link to the first search result: {search_results[0]}"
        except Exception as e:
            print(f"An error occurred during the search: {e}")

    return "I am sorry, can you repeat?"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: str = update.message.chat.type
    text:str = update.message.text

    print(f'User ({update.message.chat.id}) in {message}: "{text}"')

    if message == "group":
        if bot_username in text:
            new_text: str = text.replace(bot_username, "")
            response: str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)

    print("response sent")
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update{update} caused error {context.error}")


if __name__ == '__main__':
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('start', custom_command))
    app.add_handler(CommandHandler('start', help_command))


    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)


    print("polling")
    app.run_polling(poll_interval=3)
from asyncore import dispatcher

from telegram.ext import Updater, CommandHandler

from bot import start_command


def main():
    updater = Updater(token="YOUR_API_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start_command)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()
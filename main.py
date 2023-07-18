from asyncore import dispatcher

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final

from googlesearch import search
import mysql.connector
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

cnx = mysql.connector.connect(
    host="localhost",
    port=3307,  # Replace with the appropriate port
    user="root",
    password="12345",
    database="authors_table"
)

cursor = cnx.cursor()
query = "INSERT INTO authors (name, url) VALUES (%s, %s)"
values = ("Charles Dickens", "https://example.com/charles-dickens")
cursor.execute(query, values)
cnx.commit()
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cnx = mysql.connector.connect(
        host="localhost",
        port=3307,  # Replace with the appropriate port
        user="root",
        password="12345",
        database="authors_table"
    )

    await update.message.reply_text("Hello! What book do you want me to tell you about?")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a nice geeky bot. Tell me something to start the conversation")

def handle_user_input(text: str) -> str:
    cursor = cnx.cursor()
    query = "SELECT url FROM authors WHERE name = %s"  # Use %s as a placeholder for the name
    cursor.execute(query, (text,))  # Pass the text as a parameter to the query
    results = cursor.fetchall()

    author_url = "No URL found"  # Default value in case no URL is found in the database
    if results:
        author_url = results[0][0]  # Extract the URL from the query result

    try:
        search_results = list(search(text))
        print(len(search_results))
        if search_results:
            return f"Here is the link to the first search result: {author_url}"
    except Exception as e:
        print(f"An error occurred during the search: {e}")

    return "I am sorry, can you repeat?"


def handle_response(text: str) -> str:
    return handle_user_input(text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message}: "{text}"')

    if message == "group":
        if bot_username in text:
            new_text: str = text.replace(bot_username, "")
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("response sent")
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update{update} caused error {context.error}")


if __name__ == '__main__':


    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('start', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("polling")
    app.run_polling(poll_interval=3)


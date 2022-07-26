from logging import Filter
from telegram import *
from telegram.ext import *
from requests import *


def startCommand(update, context):

    update.message.reply_text("Hi! Welcome to NFT Minter Bot.\n\n\nPlease Enter Your Wallet (Private Key) :")
    

def private_key(update, context):

    text = str(update.message.text)
    print(text)

    # Bot response
    response = "responses.get_response(text)"
    update.message.reply_text(response)

if __name__ == "__main__":

    updater = Updater("", use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', startCommand))
    dp.add_handler(MessageHandler(Filters.text, private_key))

    # Run the bot
    updater.start_polling()
    updater.idle()

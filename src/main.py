from telegram import *
from telegram.ext import *
from requests import *
from private_key import set_private_key


def startCommand(update, context):

    update.message.reply_text("Hi! Welcome to NFT Minter Bot.\n\n\nPlease Enter Your Wallet (Private Key) :")
    

def error(update, context):

    print(f"Update {update} caused Error {context.error}")


def get_private_key(update, context):

    text = str(update.message.text)
    print(text)

    if len(text) != 64:
        response = 'Invaild private key!'
        update.message.reply_text(response)
        text = str(update.message.text)

    else:
        response = "Great! Now you can mint your NFTs."
        update.message.reply_text(response)

        username = update.message.chat.username
        set_private_key(text, username)



if __name__ == "__main__":

    updater = Updater("", use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', startCommand))
    dp.add_handler(MessageHandler(Filters.text, get_private_key))

    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling()
    updater.idle()

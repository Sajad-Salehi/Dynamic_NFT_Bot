import os
import telebot
from bottons import keyboard1, keyboard2, keyboard3
from private_key import set_private_key, get_user_info
from responses import myWallet, myAccount, addAccount, getPrivateKey, static, dynamic, mint


api_key = os.getenv('API_KEY')
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start'])
def startCommand(message):

    text = "Hi welcome to NFT minter bot.\nFirst, please set up your Wallet."
    bot.send_message(message.chat.id, text, reply_markup=keyboard1)


@bot.message_handler(func=myWallet)
def MyWallet(message):

    text = '1.Add Account:\n --> Set up your wallet account\n\n2. My Wallet Account:\n --> See your wallet info'
    bot.send_message(message.chat.id, text, reply_markup=keyboard2)


@bot.message_handler(func=myAccount)
def MyAccount(message):

    username = message.from_user.username
    wallet_addres, private_key = get_user_info(username)
    text = f'Username: @{username}\n\nWallet Address: {wallet_addres}\n\nPrivate Key: {private_key}'
    bot.send_message(message.chat.id, text, reply_markup=keyboard1)


@bot.message_handler(func=addAccount)
def addAccount(message):

    text = 'Please enter your (Private key): '  
    bot.send_message(message.chat.id, text)
    

@bot.message_handler(func=mint)
def mintNFT(message):

    bot.send_message(message.chat.id, 'Choose what kind of NFT do you want to mint: ', reply_markup=keyboard3)

@bot.message_handler(func=getPrivateKey)
def setPrivateKey(message):

    privateKey = message.text
    username = message.from_user.username
    set_private_key(username, privateKey)
    text = 'Nice! Your wallet account was added successfully. Now you can start and mint your NFTs.'
    bot.send_message(message.chat.id, text, reply_markup=keyboard1)


@bot.message_handler(func=static)
def MintStaticNFT(message):

    bot.send_message(message.chat.id, 'saaalm static')


@bot.message_handler(func=dynamic)
def MintDynamicNFT(message):

    bot.send_message(message.chat.id, 'saaalam dynamic')


bot.polling()
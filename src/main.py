import os
import telebot
from mint_static import mint_token
from mint_dynamic import set_ipfs_Uri, mint_token_
from upload_metadata import *
from bottons import keyboard1, keyboard2, keyboard3, keyboard4
from user_info import *
from responses import *


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

    if check_user_wallet(username) == False:
        text = "Sorry. You did not set up any Wallet account!"
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
        return

    wallet_addres, private_key, balance = get_user_info(username)
    text = f'Username: @{username}\n\nBalance: {balance} eth\n\nWallet Address: {wallet_addres}\n\nPrivate Key: {private_key}'
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

    username = message.from_user.username

    if check_user_wallet(username) == False:
        text = 'Sorry. You did not set up any Wallet account!'
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
        return

    info = get_user_info(username)

    if float(info[2]) < 0.05:
        text = 'You do not have enough balance to mint NFT. Please get some Eth here: https://bit.ly/3cHv5HK'
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)

    else:
        text = 'Alright. Let`s set up your NFT metadata.\nPlease send NFT image: '
        bot.send_message(message.chat.id, text)


@bot.message_handler(func=dynamic)
def MintDynamicNFT(message):

    username = message.from_user.username

    if check_user_wallet(username) == False:
        text = 'Sorry. You did not set up any Wallet account!'
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
        return

    info = get_user_info(username)

    if float(info[2]) < 0.05:
        text = 'You do not have enough balance to mint NFT. Please get some Eth here: https://bit.ly/3cHv5HK'
        bot.send_message(message.chat.id, text, reply_markup=keyboard1)
    
    else:
        text = 'Alright. Please use bottons to set up your (3 specific metadata) and then click (Mint the nft).'
        bot.send_message(message.chat.id, text, reply_markup=keyboard4)


@bot.message_handler(func=set_dynamic_metadata)
def dynamic_metadata(message):

    text = 'Please send NFT image: '
    send = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(send, get_dynamic_pics)


def get_dynamic_pics(message):
    
    username = message.from_user.username
    id = message.photo[-1].file_id
    info = bot.get_file(id)
    x = bot.download_file(info.file_path)

    image_url = upload_file(x)

    set_metadata(image_url, "image",username)
    send = bot.send_message(message.from_user.id, "Send NFT title: ")
    bot.register_next_step_handler(send, get_dynamic_name)


    
@bot.message_handler(func=check_dynamic_mint)
def mint_dynamic_nft(message):

    username = message.from_user.username
    set_ipfs_Uri(username)
    uri = mint_token_(username)
    bot.send_message(message.from_user.id, f"Nice! Your NFT minted successfully.\nSee your NFT in OpenSea: {uri}")



@bot.message_handler(content_types=['photo'])
def get_static_pics(message):
    
    username = message.from_user.username
    id = message.photo[-1].file_id
    info = bot.get_file(id)
    x = bot.download_file(info.file_path)

    image_url = upload_file(x)

    set_metadata(image_url, "image",username)
    send = bot.send_message(message.from_user.id, "Send NFT title: ")
    bot.register_next_step_handler(send, get_static_name)


@bot.message_handler(func=aboutMe)
def about_me(message):

    text = '''Hi there. My name is Sajad.
    \n- I am a Blockchain dev.\n\nI have created this bot that is use for mint dynamic NFTs.\n\n\n
    - Email: SajadSolidity@gmail.com\n- Github: github.com/sajad-salehi'''
    
    bot.send_message(message.chat.id, text)


def get_static_name(message):

    title = message.text
    username = message.from_user.username
    set_metadata(title, "name", username)
    send = bot.send_message(message.from_user.id, "Send NFT description: ")
    bot.register_next_step_handler(send, get_static_desc)


def get_static_desc(message):

    desc = message.text
    username = message.from_user.username
    set_metadata(desc, "description", username)
    metadata_url = upload_metadata(username)
    uri = mint_token(username, metadata_url)
    bot.send_message(message.from_user.id, f"Nice! Your NFT minted successfully.\nSee your NFT in OpenSea: {uri}")
    

def get_dynamic_name(message):

    title = message.text
    username = message.from_user.username
    set_metadata(title, "name", username)
    send = bot.send_message(message.from_user.id, "Send NFT description: ")
    bot.register_next_step_handler(send, get_dynamic_desc)


def get_dynamic_desc(message):

    desc = message.text
    username = message.from_user.username
    set_metadata(desc, "description", username)
    metadata_url = upload_metadata(username)
    add_dynamic_metadata(username, metadata_url)
    bot.send_message(message.from_user.id, "The metadata saved successfully.")




bot.polling()

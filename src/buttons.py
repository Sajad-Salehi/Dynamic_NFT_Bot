from telebot import types


nft_button = types.KeyboardButton('Mint NFT')
about_button = types.KeyboardButton('About me')
wallet_button = types.KeyboardButton('My Wallet')
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(wallet_button).add(nft_button).add(about_button)


myWallet_button = types.KeyboardButton('My Wallet Account')
addAccount_button = types.KeyboardButton('Add Account')
keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(addAccount_button).add(myWallet_button)


static_button = types.KeyboardButton('Mint Static NFT')
dynamic_button = types.KeyboardButton('Mint Dynamic NFT')
keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(dynamic_button).add(static_button)


metadata1 = types.KeyboardButton('1. Set up first metadata')
metadata2 = types.KeyboardButton('2. Set up second metadata')
metadata3 = types.KeyboardButton('3. Set up third metadata')
mint_button = types.KeyboardButton('4. Mint the NFT')
keyboard4 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(metadata1).add(metadata2).add(metadata3).add(mint_button)

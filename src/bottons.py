from telebot import types


nft_botton = types.KeyboardButton('Mint NFT')
about_botton = types.KeyboardButton('About me')
wallet_botton = types.KeyboardButton('My Wallet')
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(wallet_botton).add(nft_botton).add(about_botton)


myWallet_botton = types.KeyboardButton('My Wallet Account')
addAccount_botton = types.KeyboardButton('Add Account')
keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(addAccount_botton).add(myWallet_botton)


static_botton = types.KeyboardButton('Mint Static NFT')
dynamic_botton = types.KeyboardButton('Mint Dynamic NFT')
keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(dynamic_botton).add(static_botton)
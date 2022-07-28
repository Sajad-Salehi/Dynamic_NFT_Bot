import pymongo
from static import get_address
from pymongo import MongoClient



def connect_collection():

    client = MongoClient("mongodb+srv://sajad:03758403@cluster0.c15ip.mongodb.net/?retryWrites=true&w=majority")
    db = client['nft_minter_bot']
    collection = db['nft_minter_bot']

    return collection



def set_private_key(username, private_key):


    wallet_address = get_address(private_key)
    
    user_info = {

        "id": username,
        "private_key": private_key,
        "wallet_address": wallet_address
    }
    
    collection = connect_collection()
    collection.insert_one(user_info)



def get_user_info(username):

    collection = connect_collection()
    
    x = {"id": username}
    user_info = collection.find_one(x)

    return user_info['wallet_address'], user_info['private_key']




from wallet_info import get_address, get_balance
from pymongo import MongoClient



def connect_collection():

    client = MongoClient("")
    db = client['nft_minter_bot']
    collection = db['nft_minter_bot']

    return collection



def set_private_key(username, private_key):


    wallet_address = get_address(private_key)
    
    user_info = {

        "id": username,
        "user_metadata": [],
        "private_key": private_key,
        "wallet_address": wallet_address,
    }
    
    collection = connect_collection()
    collection.insert_one(user_info)



def get_user_info(username):

    collection = connect_collection()
    
    x = {"id": username}
    user_info = collection.find_one(x)
    balance = get_balance(user_info['wallet_address'])

    return user_info['wallet_address'], user_info['private_key'], balance


def set_metadata(image_url, username):

    collection = connect_collection()
    x = {"id": username}
    user_info = collection.find_one(x)

    user_info['user_metadata'].append(image_url)
    newvalues = { "$set": { "user_metadata": user_info['user_metadata'] } }
    collection.update_one(x, newvalues)
    print(user_info['user_metadata'])


def proccess_metadata(username):

    collection = connect_collection()
    x = {"id": username}
    user_info = collection.find_one(x)

    metadata = {

        "name": user_info['user_metadata'][1],
        "description": user_info['user_metadata'][2],
        "image": user_info['user_metadata'][0],
        "attributes": [{}]
    }

    newvalues = { "$set": { "user_metadata": [] } }
    collection.update_one(x, newvalues)

    return metadata


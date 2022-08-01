
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
        "private_key": private_key,
        "wallet_address": wallet_address,
        "nft_metadata": [],
        "metadata_url": []
    }
    
    collection = connect_collection()
    collection.insert_one(user_info)



def get_user_info(username):

    collection = connect_collection()
    
    x = {"id": username}
    user_info = collection.find_one(x)
    balance = get_balance(user_info['wallet_address'])

    return user_info['wallet_address'], user_info['private_key'], balance


def set_metadata(content, type, username):

    collection = connect_collection()
    x = {"id": username}
    user_info = collection.find_one(x)

    if type == 'image':

        metadata = {
            "name": None,
            "description": None,
            "image": None,
            "attributes": None
        }
        metadata['image'] = content
        user_info['nft_metadata'].append(metadata)

    else:
        user_info["nft_metadata"][-1][type] = content

    newvalues = { "$set": { "nft_metadata": user_info['nft_metadata'] } }
    collection.update_one(x, newvalues)
    print(user_info['nft_metadata'])



def check_user_wallet(username):

    collection = connect_collection()
    
    x = {"id": username}
    user_info = collection.find_one(x)
    
    if user_info == None:
        return False
    
    if user_info["wallet_address"] == None:
        return False
    
    else:
        return True


def get_nft_metadata(username):

    collection = connect_collection()
    x = {"id": username}
    user_info = collection.find_one(x)

    return user_info['nft_metadata']


def add_dynamic_metadata(username, metadata):

    collection = connect_collection()
    x = {"id": username}
    user_info = collection.find_one(x)
    user_info['metadata_url'].append(metadata)
    newvalues = { "$set": { "metadata_url": user_info['metadata_url'] } }
    collection.update_one(x, newvalues)
    print(user_info["metadata_url"])


def get_metadata_url(username):

    collection = connect_collection()
    x = {"id": username}
    user_info = collection.find_one(x)

    return user_info['metadata_url']



import os
import json
import ipfshttpclient
from userInfo import get_metadata

def upload_file():

    IPFS_CONNECT_URL = ""
    IPFS_FILE_URL = ""

    client = ipfshttpclient.connect(IPFS_CONNECT_URL)

    with open('image.jpg', 'rb') as nft_file:
        file_info = client.add(nft_file)

    nft_file_url = IPFS_FILE_URL + file_info['Hash']
    os.remove('image.jpg')
    return nft_file_url



def upload_metadata(username):

    IPFS_CONNECT_URL = ""
    IPFS_FILE_URL = ""

    client = ipfshttpclient.connect(IPFS_CONNECT_URL)
    metadata = get_metadata(username)

    with open('metadata.json', 'wb') as nft_metadata:
        json.dump(metadata, nft_metadata)
        file_info = client.add(nft_metadata)


    nft_metadata_url = IPFS_FILE_URL + file_info['Hash']
    os.remove('metadata.json')
    return nft_metadata_url

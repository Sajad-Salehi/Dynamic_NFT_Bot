import os
import json
import ipfshttpclient
from user_info import get_nft_metadata

def upload_file(x):

    IPFS_CONNECT_URL = ""
    IPFS_FILE_URL = ""

    client = ipfshttpclient.connect(IPFS_CONNECT_URL)

    with open('image.png', 'wb') as new_file:
        new_file.write(x)

    with open('image.png', 'rb') as nft_file:
        file_info = client.add(nft_file)

    nft_file_url = IPFS_FILE_URL + file_info['Hash']
    os.remove('image.png')
    return nft_file_url



def upload_metadata(username):

    IPFS_CONNECT_URL = ""
    IPFS_FILE_URL = ""

    client = ipfshttpclient.connect(IPFS_CONNECT_URL)
    metadata = get_nft_metadata(username)[-1]

    with open('metadata.json', 'w') as nft_metadata:
        json.dump(metadata, nft_metadata, indent=4)
    
    with open('metadata.json', 'rb') as nft_metadata:
        file_info = client.add(nft_metadata)


    nft_metadata_url = IPFS_FILE_URL + file_info['Hash']
    os.remove('metadata.json')
    return nft_metadata_url

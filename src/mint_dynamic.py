import os
import json
import time
from web3 import Web3
from user_info import get_user_info, get_metadata_url
from web3.middleware import geth_poa_middleware


def connect_contract(username):

    file = open('abi/dynamicMinter.json')
    data = json.load(file)
    abi = data['abi']

    user_info = get_user_info(username)
    private_key = user_info[1]
    wallet_address = user_info[0]
    contract_address = '
    '


    trx_info = {

        'w3': None,
        'nonce': None,
        'contract': None,
        'rinkeby_chain_id': 4,
        'private_key': private_key,
        'wallet_address': wallet_address,
        'contract_address': contract_address,        
    }

    w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER')))
    trx_info['w3'] = w3
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    nonce = w3.eth.getTransactionCount(trx_info['wallet_address'])
    trx_info['nonce'] = nonce
    contract = w3.eth.contract(address=contract_address, abi=abi)
    trx_info['contract'] = contract

    return trx_info



def mint_token_(username):

    trx_info = connect_contract(username)

    w3 = trx_info['w3']
    nftMinter = trx_info['contract']

    # 1. make a transaction
    create_nft = nftMinter.functions.mint_nft().buildTransaction(
        {
            "chainId": trx_info['rinkeby_chain_id'],
            "from": trx_info['wallet_address'],
            "nonce": trx_info['nonce']
        })


    # 2. sign the transaction
    sign_create_nft = w3.eth.account.sign_transaction(
        create_nft,
        private_key=trx_info['private_key'])


    # 2. send the trnsaction
    trx_hash = w3.eth.send_raw_transaction(sign_create_nft.rawTransaction)
    trx_recipt = w3.eth.wait_for_transaction_receipt(trx_hash)
    time.sleep(4)
    token_id = nftMinter.functions.getItemId().call() 
    
    opensea_url = f"https://testnets.opensea.io/assets/rinkeby/{trx_info['contract_address']}/{token_id - 1}"
    return opensea_url


def set_ipfs_Uri(username):

    uri = get_metadata_url(username)
    metadata_1 = uri[-3]
    metadata_2 = uri[-2]
    metadata_3 = uri[-1]

    trx_info = connect_contract(username)
    w3 = trx_info['w3']
    nftMinter = trx_info['contract']

    #Make transaction
    setUri_trx = nftMinter.functions.set_uri(metadata_1, metadata_2, metadata_3).buildTransaction({

        "chainId": trx_info['rinkeby_chain_id'],
        "from": trx_info['wallet_address'],
        "nonce": trx_info['nonce']
    })

    # 2. sign the transaction
    sign_setUri_trx = w3.eth.account.sign_transaction(
        setUri_trx,
        private_key=trx_info['private_key'])


    # 2. send the trnsaction
    trx_hash = w3.eth.send_raw_transaction(sign_setUri_trx.rawTransaction)
    trx_recipt = w3.eth.wait_for_transaction_receipt(trx_hash)
    time.sleep(4)

    return trx_hash

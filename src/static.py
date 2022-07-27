import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware


def connect_web3():

    file = open('nftMinter.json')
    contract_address = '0x224DC9b3B48582e4D2daAE80D9E3fc339D5C321D'

    data = json.load(file)
    abi = data["abi"]


    trx_info = {

        'w3': None,
        'nonce': None,
        'contract': None,
        'rinkeby_chain_id': 4,
        'contract_address': contract_address,
        'private_key': os.getenv('PRIVATE_KEY'),
        'provider_url': os.getenv('WEB3_PROVIDER'),
        'wallet_address': '0xB268C07881a418D0BcADCF7204CeBc6D68A54904'
    }

    # connecting to the infura http provier and create contract
    w3 = Web3(Web3.HTTPProvider(trx_info['provider_url']))
    trx_info['w3'] = w3
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    nonce = w3.eth.getTransactionCount(trx_info['wallet_address'])
    trx_info['nonce'] = nonce
    trx_info['contract_addres'] = contract_address
    contract = w3.eth.contract(address=contract_address, abi=abi)
    trx_info['contract'] = contract

    return trx_info



def mint_token():

    trx_info = connect_web3()

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
    token_id = nftMinter.functions.getItemId().call() 

    opensea_url = f"https://testnets.opensea.io/assets/rinkeby/{trx_info['contract_address']}/{token_id - 1}"
    print(opensea_url)
    return opensea_url


def set_ipfs_Uri(metadata_1, metadata_2, metadata_3):


    trx_info = connect_web3()
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

    return trx_hash



def get_address(private_key):

    w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER')))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    PA=w3.eth.account.from_key(private_key)

    # Get public address from a signer wallet
    Public_Address=PA.address
    return Public_Address


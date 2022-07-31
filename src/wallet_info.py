import os
from web3 import Web3
from web3.middleware import geth_poa_middleware



def get_address(private_key):

    w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER')))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    PA=w3.eth.account.from_key(private_key)

    # Get public address from a signer wallet
    Public_Address=PA.address
    return Public_Address


def get_balance(address):

    w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER')))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    balance = w3.eth.get_balance(address)
    ether_balance = Web3.fromWei(balance, unit='ether')
    return "%.4f"%ether_balance


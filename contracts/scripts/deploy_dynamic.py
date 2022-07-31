from brownie import accounts, nftMinter

def main():

    account = accounts.load('dev1')
    contract = nftMinter.deploy({"from": account})
    print(f"Your contract deployed at {contract}")

'''
    
    uri_1 = 'https://ipfs.io/ipfs/QmeFfKSzbfT9YJutBPFNU3pTRPfSHqfReP2xyZUCtvmTsY'
    uri_2 = 'https://ipfs.io/ipfs/QmVkfzS11dJ5WRV4tQi3LC9Gvx4QUzULydGXjSjKhBBbNr'
    uri_3 = 'https://ipfs.io/ipfs/QmUpdLbS4HpedgDkQFemB49eMCeppkZJ43mUFWv7ysnki5'

    trx = contract.set_uri(uri_1, uri_2, uri_3, {'from': account})
    trx.wait(2)
    print(trx)

    trx = contract.mint_nft({'from': account})
    trx.wait(2)
    print(trx)
    
'''
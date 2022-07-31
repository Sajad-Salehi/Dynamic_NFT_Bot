from brownie import accounts, nftMinter

def main():

    account = accounts.load('dev1')
    contract = nftMinter.deploy({"from": account})
    print(f"Your contract deployed at {contract}")


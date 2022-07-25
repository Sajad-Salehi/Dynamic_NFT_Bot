from brownie import accounts, nftMinter

def main():

    account = accounts.load('dev1')
    contract = nftMinter.deploy({"from": account}, publish_source=True)
    print(f"Your contract deployed at {contract}")

    #0x5a34EAD70355f8652DCB5bB808036ef221F5F451
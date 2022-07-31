from brownie import staticMinter, accounts

def main():

    account = accounts.load('dev1')
    contract = staticMinter.deploy({'from': account}, publish_source=False)

    print(f"Your contract deployed at {contract}")



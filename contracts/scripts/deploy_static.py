from brownie import staticMinter, accounts

def main():

    account = accounts.load('dev1')
    contract = staticMinter.deploy({'from': account}, publish_source=False)

    print(f"Your contract deployed at {contract}")


    #0xCAbE76e5d516d33C5ea000467A9F910bE158577D
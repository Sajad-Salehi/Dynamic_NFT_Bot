
    
from requests import request


def myWallet(message):

    request = message.text

    if request == 'My Wallet':
        return True

    else:
        return False    


def myAccount(message):

    request = message.text

    if request == 'My Wallet Account':
        return True

    else:
        return False  


def addAccount(message):

    request = message.text

    if request == 'Add Account':
        return True

    else:
        return False  


def getPrivateKey(message):

    request = message.text

    if len(request) == 64:
        return True

    else:
        return False  

def static(message):

    request = message.text

    if request == 'Mint Static NFT':
        return True

    else:
        return False  

def dynamic(message):

    request = message.text

    if request == 'Mint Dynamic NFT':
        return True

    else:
        return False  


def mint(message):

    request = message.text

    if request == 'Mint NFT':
        return True

    else:
        return False  


def set_dynamic_metadata(message):

    request = message.text

    if request == '1. Set up first metadata' or request == '2. Set up second metadata' or request == '3. Set up third metadata':
        return True
    
    else:
        return False


def check_dynamic_mint(message):

    request = message.text

    if request == "4. Mint the NFT":
        return True

    else:
        return False

    
def aboutMe(message):

    request = message.text

    if request == "About me":
        return True

    else:
        return False
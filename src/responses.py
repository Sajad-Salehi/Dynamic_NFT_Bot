from private_key import set_private_key, get_user_info

    
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
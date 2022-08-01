# Dynamic_NFT_bot
<h3>This is a Telegram bot that allowes you to mint dynamic NFTs.</h3><h4>I have create it by using Solidity, Chainlink keepers, OpenZeppelin and Python.</h4>

<br/><br/>
<p align="center">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/1.png" width="240" height="270">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/2.png" width="240" height="270">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/3.png" width="240" height="270">
</p><br>


## Prerequisites
Please install or have installed the following:

- [python](https://www.python.org/downloads/)
- [Telegram](https://telegram.org/)
- [metamask](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjtl7Oi6N_4AhWei_0HHbjzDH4QjBB6BAgHEAE&url=https%3A%2F%2Fmetamask.io%2Fdownload%2F&usg=AOvVaw049ASZIf5umKu9KN8vjUeH)


## Installation
[Install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), if you haven't already. Here is a simple way to install venv.

```bash
python -m pip install --user virtualenv
python -m virtualenv --help
```

Or, if that doesn't work, via pipx
```bash
pipx install virtualenv
virtualenv --help
```

Create a Virtual Environments and active venv
```bash
python3 -m virtualenv venv
cd venv/bin
source activate
```

After that you need install telebot, web3.py and ipfs that we're going to use it to store our metadata 
```bash
pip install web3
pip install eth-brownie
pip install ipfshttpclient
pip install pyTelegramBotAPI
```


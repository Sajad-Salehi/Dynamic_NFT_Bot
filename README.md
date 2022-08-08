# Dynamic_NFT_bot
<h3>This is a Telegram bot that allowes you to mint dynamic NFTs.</h3><h4>I have created this bot using Solidity, Chainlink keepers, OpenZeppelin, Python and telebot.</h4>

<br/><br/>
<p align="center">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/1.png" width="190" height="270">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/2.png" width="190" height="270">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/3.png" width="190" height="270">
</p><br>

<p align="center">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/6.png" width="290" height="300">
<img src="https://github.com/Sajad-Salehi/Dynamic_NFT_Bot/blob/main/images/5.png" width="290" height="300">
</p><br>

## Prerequisites
Please install or have installed the following:

- [Python](https://www.python.org/downloads/)
- [Telegram](https://telegram.org/)
- [Metamask](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjtl7Oi6N_4AhWei_0HHbjzDH4QjBB6BAgHEAE&url=https%3A%2F%2Fmetamask.io%2Fdownload%2F&usg=AOvVaw049ASZIf5umKu9KN8vjUeH)


## Installation
[Install virtualenv](https://virtualenv.pypa.io/en/latest/installation.html), if you haven't already. Here is a simple way to install venv.

```bash
python -m pip install --user virtualenv
python -m virtualenv --help
```
<br>
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

<br/>After that you need install telebot, web3.py and ipfs that we're going to use it to store our metadata 
```bash
pip install web3
pip install eth-brownie
pip install ipfshttpclient
pip install pyTelegramBotAPI
```

# Usage
Run this command to initalize ipfs:
```bash
ipfs daemon 
export IPFS_FILE_URL = "File_url"
export IPFS_CONNECT_URL= "Connect_url"
```

<br>Deploy the smart contract using brownie:<br>
First clone this repository and then deploy the smart contract. I prefer to use eth-brownie, but you can use whatever you want.
```bash
cd ../contracts
brownie compile
brownie run scripts/deploy_dynamic.py --network <NETWORK>
brownie run scripts/deploy_static.py --network <NETWORK>
```

<br>Now you need to set your Api_key and web3_provider(Alchemy or Infura)<br>
Use @botFather to create your bot and get Api_key
```bash
export WEB3_PROVIDER= "Web3_provider"
export API_KEY= "Api_key"
```


<br>Finally use this command to run the bot.
```bash
python3 main.py
```


## Resources


* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) To get started with Brownie
* ["Brownie documentation"](https://eth-brownie.readthedocs.io/en/stable/) For more in-depth information
* ["Getting Started with IPFS"](https://medium.com/python-pandemonium/getting-started-with-python-and-ipfs-94d14fdffd10) Getting started with python and ipfs
* ["Getting Started with web3.py"](https://medium.com/geekculture/interacting-with-ethereum-network-in-python-using-web3-py-part-4-73ee4c978626) Web3.py quickstart
* ["Introduction to ERC721 standard"](https://medium.com/blockchannel/walking-through-the-erc721-full-implementation-72ad72735f3c) ERC721 standard tutrial
* ["Getting Started with ChainLink Keepers"](https://medium.com/coinmonks/get-started-with-chainlink-keepers-477c391046d7) Chainlink keepers quickstart

## Medium article
* ["Check My Medium Article"](https://medium.com/@sajadsolidity/how-to-create-a-dynamic-nft-minter-bot-using-solidity-and-python-pt-1-c719a37b5b1f) How to build a Dynamic NFT minter bot using Solidity and Python? --Part 1.
* ["Check My Medium Article"](https://medium.com/@sajadsolidity/how-to-create-a-dynamic-nft-minter-bot-using-solidity-and-python-pt-2-f994a75cf8ee) How to build a Dynamic NFT minter bot using Solidity and Python? --Part 2.<br><br>



## License

This project is licensed under the [MIT license](LICENSE).

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";


contract dynamicMinter is ERC721URIStorage {

    using Counters for Counters.Counter;
    Counters.Counter private _tokenId;

    string[] uri;
    uint public lastTimeStamp;
    uint public immutable interval;

    mapping(address => string[]) ipfsUri;
    mapping(uint256 => uint256) id_to_currentURI;
    mapping(uint256 => string[]) id_to_ipfsUri;

    constructor() ERC721("NFT Minter", "NFT Minter") {

        interval = 30;
        lastTimeStamp = block.timestamp;
    }


    function mint_nft() public {
        
        uint256 newItemId = _tokenId.current();
        string memory tokenURI = ipfsUri[msg.sender][0];

        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        id_to_currentURI[newItemId] = 0;
        id_to_ipfsUri[newItemId] = ipfsUri[msg.sender];

        _tokenId.increment();
    }


    function getItemId() public view returns(uint256) {

        uint256 id = _tokenId.current();
        return id;
    }


    function growNFT(uint256 tokenId) private {
       

        require(id_to_currentURI[tokenId] < 2, "It id impossible to grow more");

        uint256 current_uri = id_to_currentURI[tokenId] + 1;
        string memory newUri = id_to_ipfsUri[tokenId][current_uri];

        _setTokenURI(tokenId, newUri);
        id_to_currentURI[tokenId] += 1;
    }


    function set_uri(string memory uri1, string memory uri2, string memory uri3) public {

        uri = [uri1, uri2, uri3];
        ipfsUri[msg.sender] = uri;

    }


    function checkUpkeep() external view returns (bool upkeepNeeded) {

        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;   
    }


    function performUpkeep() external {

        require(getItemId() > 0);
        if ((block.timestamp - lastTimeStamp) > interval ) {
            lastTimeStamp = block.timestamp;
            
            uint256 index = getItemId();

            for(uint256 i = 0; i < index; i++){

                growNFT(i);
            }
        }
    }

}
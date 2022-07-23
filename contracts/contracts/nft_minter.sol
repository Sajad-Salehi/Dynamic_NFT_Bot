// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract nftMinter is ERC721URIStorage {

    using Counters for Counters.Counter;
    Counters.Counter private _tokenId;

    mapping(address => string[]) IPFSuri;
    constructor() ERC721("NFT Minter", "NFT Minter") {}


    function set_metadata(

        string memory uri_0,
        string memory uri_1,
        string memory uri_2) public {

        IPFSuri[msg.sender][0] = uri_0;
        IPFSuri[msg.sender][1] = uri_1;
        IPFSuri[msg.sender][2] = uri_2;
    }

    function mint_nft() public {

        uint256 newItemId = _tokenId.current();
        string memory tokenURI = IPFSuri[msg.sender][0];

        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);

        _tokenId.increment();
    }

    function getItemId() public view returns(uint256) {
        uint256 id = _tokenId.current();
        return id;
    }
}
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {ERC721} from "../src/ERC721.sol";
contract CounterScript is Script {
    ERC721 public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new ERC721("Doge","DOGE");
        vm.stopBroadcast();
    }
}
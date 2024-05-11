// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {ERC1155} from "../src/ERC1155.sol";
contract CounterScript is Script {
    ERC1155 public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new ERC1155("BAYC","BAYC");
        vm.stopBroadcast();
    }
}
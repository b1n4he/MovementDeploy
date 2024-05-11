// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {NFTSwap} from "../src/NFTSwap.sol";
contract CounterScript is Script {
    NFTSwap public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new NFTSwap();
        vm.stopBroadcast();
    }
}
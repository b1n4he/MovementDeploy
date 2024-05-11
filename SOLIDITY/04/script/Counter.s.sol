// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {Airdrop} from "../src/Airdrop.sol";
contract CounterScript is Script {
    Airdrop public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new Airdrop();
        vm.stopBroadcast();
    }
}
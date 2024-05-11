// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {Faucet} from "../src/Faucet.sol";
contract CounterScript is Script {
    Faucet public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new Faucet(0x0000000000000000000000000000000000000000);
        vm.stopBroadcast();
    }
}
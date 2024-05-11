// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {TokenVesting} from "../src/TokenVesting.sol";
contract CounterScript is Script {
    TokenVesting public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new TokenVesting(0x0000000000000000000000000000000000000001,100);
        vm.stopBroadcast();
    }
}
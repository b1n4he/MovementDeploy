// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {Counter} from "../src/Counter.sol";
import "forge-std/console.sol";
contract InteractScript is Script {
    Counter public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = Counter(0x000000000);
        counter.setNumber(1);
        console.log("Number is now: ", counter.number());
        counter.increment();
        console.log("Number was incremented to: ", counter.number());
        vm.stopBroadcast();
    }
}
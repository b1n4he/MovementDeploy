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
        counter = Counter(0x27DEC40c74152AE5E7E5B0B8190d676aBCD5887F);
        counter.setNumber(1);
        console.log("Number is now: ", counter.number());
        counter.increment();
        console.log("Number was incremented to: ", counter.number());
        vm.stopBroadcast();
    }
}
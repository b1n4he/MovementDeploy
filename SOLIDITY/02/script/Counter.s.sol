// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {ERC20} from "../src/ERC20.sol";
contract CounterScript is Script {
    ERC20 public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new ERC20("Ether","ETH");
        vm.stopBroadcast();
    }
}
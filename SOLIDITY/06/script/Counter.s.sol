// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {MerkleTree} from "../src/MerkleTree.sol";
contract CounterScript is Script {
    MerkleTree public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new MerkleTree("WTF MerkleTree","WTF",0xeeefd63003e0e702cb41cd0043015a6e26ddb38073cc6ffeb0ba3e808ba8c097);
        vm.stopBroadcast();
    }
}
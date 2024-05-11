// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;
import {Script} from "forge-std/Script.sol";
import {SignatureNFT} from "../src/Signature.sol";
contract CounterScript is Script {
    SignatureNFT public counter;
    uint256 public deployerPrivateKey = vm.envUint("PRIVATE_KEY");
    function run() public {
        vm.startBroadcast(deployerPrivateKey);
        counter = new SignatureNFT("WTF Signature","WTF",0xe16C1623c1AA7D919cd2241d8b36d9E79C1Be2A2);
        vm.stopBroadcast();
    }
}
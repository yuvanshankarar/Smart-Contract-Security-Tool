// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

/*
 ███████╗███╗   ██╗████████╗██████╗ ██╗   ██╗
 ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚██╗ ██╔╝
 █████╗  ██╔██╗ ██║   ██║   ██████╔╝ ╚████╔╝
 ██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗  ╚██╔╝
 ███████╗██║ ╚████║   ██║   ██║  ██║   ██║
 ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝
 ⚠️ VULNERABLE SMART CONTRACT
*/

contract VulnerableBank {

    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value; // ❌ Overflow risk
    }

    function withdraw(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // ❌ Re-entrancy vulnerability
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");

        balances[msg.sender] -= _amount;
    }
}

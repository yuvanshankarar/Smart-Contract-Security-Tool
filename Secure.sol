// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

contract SecureBank {

    mapping(address => uint256) private balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Low balance");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }
}

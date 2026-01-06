# Smart-Contract-Security-Tool
blockchain smart-contracts solidity ethereum security static-analysis python web3
## Smart Contract Security Analyzer

This project is a Python-based static analysis tool designed to identify common security vulnerabilities in Solidity smart contracts, including re-entrancy, integer overflow, and front-running risks. The tool analyzes contract source code and generates a security report with risk levels and recommendations.

SmartContractSecurityTool/
│
├── contracts/
│   ├── Vulnerable.sol
│   └── Secure.sol
│
├── analyzer/
│   ├── security_banner.py
│   ├── reentrancy_detector.py
│   ├── overflow_detector.py
│   └── frontrunning_detector.py
│
├── reports/
│   └── final_report.txt
│
├── main.py
├── requirements.txt
└── README.md

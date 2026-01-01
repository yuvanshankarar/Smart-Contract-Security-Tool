def detect_overflow(code):
    print("🔢 Checking for Integer Overflow...\n")

    if "pragma solidity ^0.8" in code:
        print("✅ SAFE: Solidity 0.8+ has built-in overflow checks\n")
        return "SAFE"
    else:
        print("❌ MEDIUM RISK: Solidity <0.8 (Overflow possible)\n")
        return "MEDIUM"


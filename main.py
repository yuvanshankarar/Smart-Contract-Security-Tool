from analyzer.security_banner import show_banner
from analyzer.reentrancy_detector import detect_reentrancy
from analyzer.overflow_detector import detect_overflow
from analyzer.frontrunning_detector import detect_frontrunning

CONTRACT_PATH = "contracts/Vulnerable.sol"

def main():
    show_banner()

    with open(CONTRACT_PATH, "r", encoding="utf-8", errors="ignore") as file:
        code = file.read()

    reentrancy = detect_reentrancy(CONTRACT_PATH)
    overflow = detect_overflow(code)
    frontrun = detect_frontrunning(code)

    with open("reports/final_report.txt", "w",encoding="utf-8") as report:
        report.write(f"""
SMART CONTRACT SECURITY REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Re-Entrancy Risk  : {reentrancy}
Overflow Risk    : {overflow}
Front-Running    : {frontrun}

Recommendation:
✔ Use Solidity ^0.8.0
✔ Follow Checks-Effects-Interactions
✔ Avoid public price-based logic
""")

    print("📄 Final Report Generated → reports/final_report.txt")
    print("✅ Analysis Complete!")

if __name__ == "__main__":
    main()

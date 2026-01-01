import subprocess

def detect_reentrancy(contract_path):
    print("🔁 Checking for Re-Entrancy...\n")
    result = subprocess.run(
        ["slither", contract_path],
        capture_output=True,
        text=True
    )

    if "reentrancy" in result.stdout.lower():
        print("❌ HIGH RISK: Re-Entrancy Vulnerability Detected!\n")
        return "HIGH"
    else:
        print("✅ SAFE: No Re-Entrancy Found\n")
        return "SAFE"

def detect_frontrunning(code):
    print("🏎️ Checking for Front-Running...\n")

    keywords = ["public", "price", "bid", "trade"]

    for word in keywords:
        if word in code:
            print("⚠️ LOW RISK: Potential Front-Running Detected\n")
            return "LOW"

    print("✅ SAFE: No Front-Running Pattern Found\n")
    return "SAFE"

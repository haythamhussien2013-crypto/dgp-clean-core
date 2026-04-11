def analyze_logs():
    try:
        with open("data/logs/system.log", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return {}

    stats = {}

    for line in lines:
        if "DDoS" in line:
            stats["DDoS"] = stats.get("DDoS", 0) + 1
        elif "SQL Injection" in line:
            stats["SQL Injection"] = stats.get("SQL Injection", 0) + 1
        elif "Phishing" in line:
            stats["Phishing"] = stats.get("Phishing", 0) + 1

    return stats

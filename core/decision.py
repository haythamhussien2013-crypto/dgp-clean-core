def decide_action(attack):
    if attack == "DDoS":
        return "Activate Firewall & Rate Limiting"

    elif attack == "SQL Injection":
        return "Sanitize Inputs & Block IP"

    elif attack == "Phishing":
        return "Alert User & Block Domain"

    else:
        return "Monitor & Log"

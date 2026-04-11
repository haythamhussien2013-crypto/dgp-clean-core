from cyber.attack_simulator import simulate_attack
from core.decision import decide_action
from core.learning import analyze_logs


def log_event(attack, decision):
    with open("data/logs/system.log", "a") as f:
        f.write(f"[ATTACK]: {attack} | [DECISION]: {decision}\n")


def calculate_risk(attack):
    risk_map = {
        "DDoS": 90,
        "SQL Injection": 85,
        "Phishing": 70
    }
    return risk_map.get(attack, 50)


def run_system():
    attack = simulate_attack()
    risk = calculate_risk(attack)
    decision = decide_action(attack)

    print("=== DGP SYSTEM v2 ===")
    print("Attack:", attack)
    print("Risk Level:", risk)
    print("Decision:", decision)

    log_event(attack, decision)

    # 👇 هنا الصح
    stats = analyze_logs()
    print("=== Learning Stats ===")
    print(stats)

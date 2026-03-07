from core.hachiclaw_core import HachiClawCore

# Simulated user trading behavior data
user_behavior_example = {
    "trade_frequency": 15,
    "leverage_change": 3,
    "recent_losses": 3,
    "position_size_change": 2
}

def run_simulation():

    system = HachiClawCore()

    print("🐺 Running HachiClaw AI behavioral analysis...\n")

    result = system.process_user_activity(user_behavior_example)

    print("Behavior Score:", result["behavior_score"])
    print("Risk State:", result["risk_state"])

    if result["risk_state"] == "HIGH_RISK":
        print("⚠️ Guardian Mode Activated")

    elif result["risk_state"] == "LEARNING_MOMENT":
        print("📘 Educational prompt suggested")

    else:
        print("✅ Normal trading behavior detected")


if __name__ == "__main__":
    run_simulation()

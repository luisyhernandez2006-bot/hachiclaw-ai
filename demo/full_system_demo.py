from core.hachiclaw_core import HachiClawCore

# Example simulated user behavior
user_behavior = {
    "recent_losses": 3,
    "trade_frequency": 15,
    "leverage_change": 2,
    "position_size_change": 2
}

def run_demo():

    print("🐺 HachiClaw AI - Behavioral Intelligence Demo\n")
    print("--------------------------------------------\n")

    system = HachiClawCore()

    result = system.process_user_activity(user_behavior)

    print("Behavior Score:", result["behavior_score"])
    print("Risk State:", result["risk_state"])

    print("\nBehavioral Footprint:")
    for f in result["footprint"]:
        print("-", f)

    print("\nGuardian Mode:", result["guardian"]["guardian_mode"])
    print(result["guardian"]["message"])

    if result["guardian"]["suggestion"]:
        print("Suggestion:", result["guardian"]["suggestion"])


if __name__ == "__main__":
    run_demo()






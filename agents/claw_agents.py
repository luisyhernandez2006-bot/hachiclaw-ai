"""
HachiClaw AI
Multi-Claw Agent System

Each agent performs a specialized task in the behavioral
protection ecosystem.

Author: HachiClaw AI
"""


class ClawGuardian:

    def intervene(self, risk_level):

        if risk_level == "low":
            return "No intervention required."

        if risk_level == "medium":
            return "Reminder: Consider reducing position size."

        if risk_level == "high":
            return "Guardian Alert: Emotional trading detected. Suggest cooldown."


class ClawEducator:

    def deliver_capsule(self, topic):

        capsules = {
            "revenge_trading": "Capsule: Revenge trading often increases losses.",
            "overtrading": "Capsule: Frequent trades increase fees and emotional pressure.",
            "risk_management": "Capsule: Risk only what you can afford to lose."
        }

        return capsules.get(topic, "Educational capsule not found.")


class ClawTracker:

    def analyze_behavior(self, trade_frequency, losses_in_row):

        if trade_frequency > 15:
            return "Behavior Pattern: Possible overtrading detected."

        if losses_in_row >= 3:
            return "Behavior Pattern: Emotional reaction risk."

        return "Behavior Pattern: Stable"


class ClawOpportunity:

    def detect_learning_moment(self, behavior_score):

        if behavior_score < 60:
            return "Opportunity: Good moment to review risk management."

        return "Opportunity: Continue learning and trading responsibly."


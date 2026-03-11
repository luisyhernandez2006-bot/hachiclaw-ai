class BehavioralEngine:

    def __init__(self):
        # Weight of each behavioral signal
        self.weights = {
            "recent_losses": 0.35,
            "trade_frequency": 0.25,
            "leverage_change": 0.25,
            "position_size_change": 0.15
        }

    def normalize(self, value, max_value):
        """
        Normalize a value between 0 and 1.
        """
        return min(value / max_value, 1)

    def analyze_behavior(self, user_data):
        """
        Calculates a behavioral risk score between 0.0 and 1.0
        based on trading activity patterns.
        """

        losses_score = self.normalize(user_data.get("recent_losses", 0), 5)
        frequency_score = self.normalize(user_data.get("trade_frequency", 0), 20)
        leverage_score = self.normalize(user_data.get("leverage_change", 0), 5)
        position_score = self.normalize(user_data.get("position_size_change", 0), 5)

        behavior_score = (
            losses_score * self.weights["recent_losses"] +
            frequency_score * self.weights["trade_frequency"] +
            leverage_score * self.weights["leverage_change"] +
            position_score * self.weights["position_size_change"]
        )

        return round(behavior_score, * 100)

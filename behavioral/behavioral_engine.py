"""
HachiClaw AI
Behavioral Intelligence Engine

This module analyzes user trading behavior patterns instead of market prices.
The goal is to detect emotional or impulsive behavior before it damages capital.

Core idea:
Retail traders rarely lose because of lack of information.
They lose because of behavioral escalation.

Author: HachiClaw AI
"""

class BehavioralEngine:

    def __init__(self):
        self.behavior_score = 100  # 100 = emotionally stable
        self.trade_history = []

    def register_trade(self, trade):
        """
        trade format example:
        {
            "profit": -50,
            "size": 200,
            "leverage": 10,
            "time_since_last_trade": 5
        }
        """

        self.trade_history.append(trade)

        self._update_behavior_score(trade)

        return self.behavior_score


    def _update_behavior_score(self, trade):
        """
        Updates the behavioral stability score.
        Lower score = higher emotional risk.
        """

        # Loss penalty
        if trade["profit"] < 0:
            self.behavior_score -= 5

        # Large position penalty
        if trade["size"] > 0.2:  # >20% of capital
            self.behavior_score -= 10

        # High leverage penalty
        if trade["leverage"] > 5:
            self.behavior_score -= 10

        # Impulsive frequency penalty
        if trade["time_since_last_trade"] < 10:
            self.behavior_score -= 5

        # Prevent negative values
        if self.behavior_score < 0:
            self.behavior_score = 0


    def get_behavior_state(self):
        """
        Returns the emotional trading state
        """

        if self.behavior_score >= 80:
            return "Stable"

        elif self.behavior_score >= 60:
            return "Elevated Risk"

        elif self.behavior_score >= 40:
            return "Impulsive Behavior"

        else:
            return "Critical Emotional Trading"

class GuardianMode:

    def __init__(self):
        self.active = False

    def activate(self, behavior_score):
        """
        Activates guardian protection based on the 0-100 behavior score.
        """
        if behavior_score >= 80:
            self.active = True
            return {
                "guardian_mode": "ACTIVE",
                "message": "⚠️ Emotional escalation detected.",
                "suggestion": "Pause trading briefly and review risk exposure."
            }

        elif behavior_score >= 50:
            return {
                "guardian_mode": "WATCH",
                "message": "⚡ Risky behavior pattern detected.",
                "suggestion": "Consider reviewing position sizing and leverage."
            }

        else:
            self.active = False
            return {
                "guardian_mode": "OFF",
                "message": "Normal trading behavior detected.",
                "suggestion": None
            }

class EmotionalCircuitBreaker:

def __init__(self):
self.cooldown_active = False
self.cooldown_time = 0

def evaluate_risk(self, behavior_score):
"""
Determines if intervention is required.
"""

if behavior_score >= 80:
return "STABLE", self._stable_state()

elif behavior_score >= 60:
return "ELEVATED_RISK", self._risk_warning()

elif behavior_score >= 40:
return "LEARNING_MOMENT", self._impulse_protection()

else:
return "HIGH_RISK", self._critical_lock()


def _stable_state(self):

return {
"status": "Stable",
"message": "Trading behavior is stable.",
"action": "None"
}


def _risk_warning(self):

return {
"status": "Elevated Risk",
"message": "Your trading behavior shows increased risk exposure.",
"action": "Display awareness notification"
}


def _impulse_protection(self):

return {
"status": "Impulsive Behavior",
"message": "Trading frequency and risk exposure suggest impulsive decisions.",
"action": "Suggest cooldown + show educational capsule"
}


def _critical_lock(self):

self.cooldown_active = True
self.cooldown_time = 15

return {
"status": "Critical Emotional Trading",
"message": "High emotional trading detected.",
"action": "Activate cooldown period"
}

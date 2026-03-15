"""
HachiClaw AI - Emotional Circuit Breaker
Determines the level of intervention based on the behavioral score.
Author: SoyCryptoGirl.
"""

class EmotionalCircuitBreaker:

	def __init__(self):
		self.cooldown_active = False
		self.cooldown_time = 0

	def evaluate_risk(self, behavior_score):
		"""
		Determines if intervention is required based on the score (0-100).
		High Score = High Risk.
		"""
		# 1. CRITICAL RISK (Score 80-100)
		if behavior_score >= 80:
			return "HIGH_RISK", self._critical_lock()
		# 2. LEARNING MOMENT (Score 60-79)
		elif behavior_score >= 60:
			return "LEARNING_MOMENT", self._impulse_protection()
		# 3. ELEVATED RISK (Score 40-59)
		elif behavior_score >= 40:
			return "ELEVATED_RISK", self._risk_warning()
		# 4. STABLE STATE (Score 0-39)
		else:
			return "STABLE", self._stable_state()

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
		return {
			"status": "Critical Risk",
			"message": "Critical emotional levels detected. Guardian intervention active.",
			"action": "Full account lockdown + forced cooldown"
		}

from behavioral.behavioral_engine import BehavioralEngine
from risk.emotional_circuit_breaker import EmotionalCircuitBreaker
from guardian.guardian_mode import GuardianMode
from tracking.behavioral_footprint import BehavioralFootprintTracker
from agents.claw_agents import ClawGuardian, ClawEducator


class HachiClawCore:

    def __init__(self):
        self.behavior_engine = BehavioralEngine()
        self.risk_engine = EmotionalCircuitBreaker()
        self.guardian = GuardianMode()
        self.footprint_tracker = BehavioralFootprintTracker()

        self.guardian_agent = ClawGuardian()
        self.educator_agent = ClawEducator()

    def process_user_activity(self, user_data):

        # 1️⃣ Analyze behavior
        behavior_score = self.behavior_engine.analyze_behavior(user_data)

        # 2️⃣ Generate behavioral footprint
        footprint = self.footprint_tracker.generate_footprint(user_data)

        # 3️⃣ Evaluate risk level
        risk_state = self.risk_engine.evaluate_risk(behavior_score)

        # 4️⃣ Activate Guardian Mode
        guardian_state = self.guardian.activate(behavior_score)

        # 5️⃣ Agents react
        if risk_state == "HIGH_RISK":
            self.guardian_agent.intervene("high")

        elif risk_state == "LEARNING_MOMENT":
            self.educator_agent.deliver_capsule("risk_managment")

        return {
            "behavior_score": behavior_score,
            "risk_state": risk_state,
            "footprint": footprint,
            "guardian": guardian_state
        }


class BehavioralFootprintTracker:

    def __init__(self):
        pass

    def generate_footprint(self, user_data):

        footprint = []

        if user_data.get("recent_losses", 0) >= 3:
            footprint.append("loss_cycle_detected")

        if user_data.get("trade_frequency", 0) > 10:
            footprint.append("high_trade_frequency")

        if user_data.get("leverage_change", 0) >= 2:
            footprint.append("leverage_spike")

        if user_data.get("position_size_change", 0) >= 2:
            footprint.append("position_size_escalation")

        return footprint

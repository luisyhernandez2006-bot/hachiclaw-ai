class EmotionalCircuitBreaker:
    """
    Detects emotional trading patterns.
    """

    def detect_revenge_trading(self, loss_streak, trade_frequency):

        if loss_streak >= 3 and trade_frequency > 5:
            return "Warning: possible revenge trading detected."

        return "Behavior stable."

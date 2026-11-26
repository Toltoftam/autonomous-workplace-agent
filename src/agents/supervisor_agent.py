class SupervisorAgent:

    def evaluate(self, action):

        high_risk_actions = [
            "refund",
            "payment",
            "contract"
        ]

        return action in high_risk_actions

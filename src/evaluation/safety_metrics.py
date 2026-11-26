class SafetyMetrics:

    def calculate_success_rate(
        self,
        safe_actions,
        total_actions
    ):

        if total_actions == 0:
            return 0

        return round(
            safe_actions /
            total_actions *
            100,
            2
        )

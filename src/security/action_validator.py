class ActionValidator:

    @staticmethod
    def validate(action):

        approved_actions = [
            "send_email",
            "generate_report",
            "create_lead",
            "schedule_followup"
        ]

        return action in approved_actions

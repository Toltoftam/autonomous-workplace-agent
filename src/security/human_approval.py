class HumanApproval:

    critical_actions = [
        "send_refund",
        "delete_customer",
        "sign_contract"
    ]

    @classmethod
    def requires_approval(cls, action):

        return action in cls.critical_actions

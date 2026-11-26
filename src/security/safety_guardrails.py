class SafetyGuardrails:

    BLOCKED_INTENTS = [
        "transfer_money",
        "share_password",
        "disable_security_controls"
    ]

    @classmethod
    def is_safe(cls, intent):

        return intent not in cls.BLOCKED_INTENTS

from enum import Enum


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class PolicyEngine:

    HIGH_RISK_ACTIONS = [
        "send_payment",
        "issue_refund",
        "delete_customer",
        "modify_contract",
        "release_confidential_data"
    ]

    @classmethod
    def assess_action(cls, action):

        if action in cls.HIGH_RISK_ACTIONS:
            return RiskLevel.HIGH

        return RiskLevel.LOW

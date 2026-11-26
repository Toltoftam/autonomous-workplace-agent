from security.policy_engine import (
    PolicyEngine
)


def test_high_risk_action():

    result = (
        PolicyEngine.assess_action(
            "issue_refund"
        )
    )

    assert result.value == "high"

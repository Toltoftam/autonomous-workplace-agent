from agents.email_agent import EmailAgent


def test_refund_classification():

    agent = EmailAgent()

    result = agent.execute(
        "I need a refund"
    )

    assert result == "refund_request"

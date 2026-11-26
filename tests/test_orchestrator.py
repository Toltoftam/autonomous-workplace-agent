from agents.workflow_orchestrator import (
    WorkflowOrchestrator
)


def test_orchestrator():

    orchestrator = (
        WorkflowOrchestrator()
    )

    result = orchestrator.execute(
        "customer_support"
    )

    assert (
        result["next_step"]
        ==
        "CustomerSupportAgent"
    )

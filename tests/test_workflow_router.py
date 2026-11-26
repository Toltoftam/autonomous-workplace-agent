from agents.task_router import (
    TaskRouter
)


def test_sales_routing():

    router = TaskRouter()

    result = router.route(
        "sales"
    )

    assert (
        result
        ==
        "LeadGenerationAgent"
    )

from src.agents.task_router import TaskRouter


class WorkflowOrchestrator:

    def __init__(self):

        self.router = TaskRouter()

    def execute(
        self,
        classification
    ):

        destination = self.router.route(
            classification
        )

        return {
            "next_step": destination
        }

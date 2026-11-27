from src.agents.reporting_agent import (
    ReportingAgent
)


class ReportingWorkflow:

    def __init__(self):

        self.agent = (
            ReportingAgent()
        )

    def run(self, metrics):

        return self.agent.execute(metrics)

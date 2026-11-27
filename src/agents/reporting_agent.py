from src.agents.base_agent import BaseAgent


class ReportingAgent(BaseAgent):

    def __init__(self):
        super().__init__("ReportingAgent")

    def execute(self, metrics):

        return {
            "emails_processed": metrics.get(
                "emails_processed", 0
            ),
            "support_cases": metrics.get(
                "support_cases", 0
            )
        }

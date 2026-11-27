from src.agents.customer_support_agent import (
    CustomerSupportAgent
)


class CustomerSupportWorkflow:

    def __init__(self):

        self.agent = (
            CustomerSupportAgent()
        )

    def run(self, issue):

        return self.agent.execute(issue)

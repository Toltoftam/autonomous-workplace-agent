from agents.lead_generation_agent import (
    LeadGenerationAgent
)


class LeadGenerationWorkflow:

    def __init__(self):

        self.agent = (
            LeadGenerationAgent()
        )

    def run(self, company):

        return self.agent.execute(company)
      

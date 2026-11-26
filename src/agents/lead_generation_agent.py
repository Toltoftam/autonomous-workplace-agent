from agents.base_agent import BaseAgent


class LeadGenerationAgent(BaseAgent):

    def __init__(self):
        super().__init__("LeadGenerationAgent")

    def execute(self, company):

        return {
            "company": company,
            "lead_score": 80,
            "qualified": True
        }

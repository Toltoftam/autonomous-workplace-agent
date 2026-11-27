from src.agents.base_agent import BaseAgent


class EmailAgent(BaseAgent):

    def __init__(self):
        super().__init__("EmailAgent")

    def execute(self, email_text):

        email_text = email_text.lower()

        if "refund" in email_text:
            return "refund_request"

        if "help" in email_text:
            return "customer_support"

        if "pricing" in email_text:
            return "sales"

        return "general"

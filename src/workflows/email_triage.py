from src.agents.email_agent import EmailAgent
from src.security.audit_logger import AuditLogger


class EmailTriageWorkflow:

    def __init__(self):

        self.email_agent = EmailAgent()
        self.logger = AuditLogger()

    def run(self, email):

        classification = self.email_agent.execute(
            email
        )

        self.logger.log(
            action="email_classified",
            result=classification
        )

        return {
            "classification": classification
        }

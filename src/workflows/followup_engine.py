from datetime import datetime


class FollowUpEngine:

    def create_followup(
        self,
        customer
    ):

        return {

            "customer":
                customer,

            "created":
                datetime.utcnow()
                .isoformat(),

            "status":
                "pending"
        }

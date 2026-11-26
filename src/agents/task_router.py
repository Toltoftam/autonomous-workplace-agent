class TaskRouter:

    def route(self, classification):

        routes = {

            "customer_support":
                "CustomerSupportAgent",

            "sales":
                "LeadGenerationAgent",

            "refund_request":
                "HumanReviewQueue",

            "general":
                "ReportingAgent"
        }

        return routes.get(
            classification,
            "ReportingAgent"
        )

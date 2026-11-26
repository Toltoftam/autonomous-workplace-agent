class ReportingService:

    def generate_report(
        self,
        data
    ):

        return {

            "records":
                len(data),

            "status":
                "generated"
        }

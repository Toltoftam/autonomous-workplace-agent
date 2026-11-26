class EmailService:

    def send_email(

        self,
        recipient,
        subject,
        message

    ):

        return {

            "recipient":
                recipient,

            "subject":
                subject,

            "status":
                "queued"
        }

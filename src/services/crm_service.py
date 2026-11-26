class CRMService:

    def lookup_customer(
        self,
        customer_id
    ):

        return {

            "customer_id":
                customer_id,

            "status":
                "active"
        }

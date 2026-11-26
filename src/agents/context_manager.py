class ContextManager:

    def build_context(
        self,
        customer,
        interaction_history
    ):

        return {

            "customer": customer,

            "history":
                interaction_history,

            "interaction_count":
                len(interaction_history)
        }

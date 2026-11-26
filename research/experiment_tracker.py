from datetime import datetime


class ExperimentTracker:

    def __init__(self):

        self.results = []

    def save_result(
        self,
        experiment,
        outcome
    ):

        self.results.append(

            {
                "experiment": experiment,
                "outcome": outcome,
                "timestamp":
                    datetime.utcnow().isoformat()
            }

        )

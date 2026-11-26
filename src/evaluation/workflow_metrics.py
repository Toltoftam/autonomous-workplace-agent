class WorkflowMetrics:

    def evaluate(

        self,

        completed,

        total

    ):

        if total == 0:

            return 0

        return (

            completed
            /
            total
        ) * 100

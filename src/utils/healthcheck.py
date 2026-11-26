class HealthCheck:

    @staticmethod
    def status():

        return {

            "service":
                "online",

            "database":
                "online",

            "agents":
                "online"
        }

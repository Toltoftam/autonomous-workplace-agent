class EmailAgent:
    def classify(self,text):
        return "customer_support" if "help" in text.lower() else "general"
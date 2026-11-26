class RiskScorer:

    def score_email(self, content):

        score = 0

        suspicious_keywords = [
            "override",
            "ignore",
            "password",
            "credentials",
            "wire transfer",
            "payment"
        ]

        for keyword in suspicious_keywords:

            if keyword in content.lower():
                score += 25

        return min(score, 100)

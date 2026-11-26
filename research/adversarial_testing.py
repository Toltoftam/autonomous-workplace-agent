class AdversarialTestingSuite:

    def evaluate_email(self, text):

        findings = []

        if "password" in text.lower():

            findings.append(
                "credential_request"
            )

        if "ignore instructions" in text.lower():

            findings.append(
                "prompt_injection"
            )

        return findings

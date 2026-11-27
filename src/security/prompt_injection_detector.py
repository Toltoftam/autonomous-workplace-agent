class PromptInjectionDetector:

    DANGEROUS_PATTERNS = [
        "ignore previous instructions",
        "reveal system prompt",
        "override policy",
        "disable safeguards"
    ]

    @classmethod
    def scan(cls, text):

        text = text.lower()

        for pattern in cls.DANGEROUS_PATTERNS:

            if pattern in text:
                return True

        return False

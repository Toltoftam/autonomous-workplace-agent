class PromptInjectionDetector:

    DANGEROUS_PATTERNS = [

        "ignore previous instructions",

        "reveal system prompt",

        "override policy",

        "disable safeguards"
    ]

    @classmethod
    def scan(cls, text):

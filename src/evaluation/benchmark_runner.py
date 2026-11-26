from evaluation.prompt_injection_tests import TEST_CASES
from security.prompt_injection_detector import (
    PromptInjectionDetector
)


class BenchmarkRunner:

    def run(self):

        results = []

        for test in TEST_CASES:

            detected = (
                PromptInjectionDetector.scan(
                    test
                )
            )

            results.append(
                {
                    "prompt": test,
                    "detected": detected
                }
            )

        return results

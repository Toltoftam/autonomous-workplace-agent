from src.utils.healthcheck import (
    HealthCheck
)


def test_health():

    result = (
        HealthCheck.status()
    )

    assert (
        result["service"]
        ==
        "online"
    )

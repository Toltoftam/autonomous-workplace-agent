from src.utils.healthcheck import (
    HealthCheck
)

@app.get("/health")

def health():

    return HealthCheck.status()

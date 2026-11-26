import os


class Settings:

    APP_ENV = os.getenv(
        "APP_ENV",
        "development"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    SMTP_HOST = os.getenv(
        "SMTP_HOST"
    )

    SMTP_PORT = os.getenv(
        "SMTP_PORT"
    )

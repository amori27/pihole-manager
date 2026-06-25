import os


class Settings:
    pihole_host: str = os.getenv("PIHOLE_HOST", "localhost")
    pihole_port: int = int(os.getenv("PIHOLE_PORT", "80"))
    pihole_password: str | None = os.getenv("PIHOLE_PASSWORD")
    api_token: str | None = os.getenv("PIHOLE_API_TOKEN")
    refresh_interval: int = int(os.getenv("REFRESH_INTERVAL", "300"))


settings = Settings()

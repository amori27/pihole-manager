from src.core.config import settings


def test_defaults():
    assert settings.pihole_host == "localhost"
    assert settings.pihole_port == 80
    assert settings.refresh_interval >= 0

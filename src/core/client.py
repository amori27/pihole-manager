"""Pi-hole API client."""

import httpx
from src.core.config import settings


BASE_URL = f"http://{settings.pihole_host}:{settings.pihole_port}/admin/api.php"


def get_summary() -> dict:
    params = {"summary": "true"}
    if settings.api_token:
        params["auth"] = settings.api_token
    r = httpx.get(BASE_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def get_query_types() -> dict:
    params = {"getQueryTypes": "true"}
    if settings.api_token:
        params["auth"] = settings.api_token
    r = httpx.get(BASE_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def enable():
    params = {"enable": "true"}
    if settings.api_token:
        params["auth"] = settings.api_token
    httpx.get(BASE_URL, params=params, timeout=10)


def disable(seconds: int = 300):
    params = {"disable": str(seconds)}
    if settings.api_token:
        params["auth"] = settings.api_token
    httpx.get(BASE_URL, params=params, timeout=10)

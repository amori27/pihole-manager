from pydantic import BaseModel


class DomainRequest(BaseModel):
    domain: str


class BlocklistResponse(BaseModel):
    domain: str
    total: int


class HealthResponse(BaseModel):
    status: str
    pihole_connected: bool
    queries_blocked_today: int | None = None

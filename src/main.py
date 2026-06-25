from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.client import get_summary, enable, disable
from src.core.blocklist import BlocklistManager

app = FastAPI(title="Pi-hole Manager", version="1.0.0")
blocklist = BlocklistManager()


class DomainRequest(BaseModel):
    domain: str


@app.get("/health")
def health():
    try:
        summary = get_summary()
        blocked = int(summary.get("ads_blocked_today", 0))
        return {"status": "ok", "pihole_connected": True, "queries_blocked_today": blocked}
    except Exception as e:
        return {"status": "degraded", "pihole_connected": False, "error": str(e)}


@app.get("/stats")
def stats():
    return get_summary()


@app.post("/blocklist/add")
def add_domain(req: DomainRequest):
    ok = blocklist.add_domain(req.domain)
    if not ok:
        raise HTTPException(409, f"Domain already in blocklist: {req.domain}")
    return {"domain": req.domain, "total": blocklist.count()}


@app.get("/blocklist")
def list_blocklist():
    return {"domains": blocklist.list_domains(), "total": blocklist.count()}


@app.post("/pihole/enable")
def pihole_enable():
    enable()
    return {"status": "enabled"}


@app.post("/pihole/disable")
def pihole_disable(seconds: int = 300):
    disable(seconds)
    return {"status": f"disabled for {seconds}s"}

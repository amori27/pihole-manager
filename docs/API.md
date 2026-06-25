# API Reference

## `GET /health`

```json
{"status": "ok", "pihole_connected": true, "queries_blocked_today": 142}
```

## `GET /stats`

Pi-hole summary statistics.

## `POST /blocklist/add`

Add a domain to the blocklist.

**Request:**
```json
{"domain": "tracker.example.com"}
```

## `GET /blocklist`

List blocked domains.

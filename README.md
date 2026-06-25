# Pi-hole Manager

[![CI/CD](https://github.com/amori27/pihole-manager/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/amori27/pihole-manager/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)(LICENSE)
[![Docker](https://img.shields.io/badge/docker-compose-blue)]()

> Infrastructure-as-Code management layer for Pi-hole. FastAPI backend with Pi-hole API integration for DNS analytics, dynamic blocklist management, and one-click docker-compose deployment.

## Features

- Pi-hole API client (summary, query types, enable/disable)
- Dynamic blocklist manager (add/remove/list domains)
- One-command docker-compose deployment with healthchecks
- REST API for all operations

## Quick Start

```bash
# Start Pi-hole + Manager
export PIHOLE_PASSWORD=your-secure-password
docker compose -f docker/docker-compose.yml up -d

# Check health
curl http://localhost:8000/health

# Block a domain
curl -X POST http://localhost:8000/blocklist/add \
  -H "Content-Type: application/json" \
  -d '{"domain": "tracker.example.com"}'

# View stats
curl http://localhost:8000/stats
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Health + Pi-hole status |
| GET | `/stats` | Pi-hole summary |
| POST | `/blocklist/add` | Add domain to blocklist |
| GET | `/blocklist` | List blocked domains |
| POST | `/pihole/enable` | Enable Pi-hole |
| POST | `/pihole/disable` | Disable Pi-hole (default 300s) |

## License

MIT

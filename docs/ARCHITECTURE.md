# Pi-hole Manager — Architecture

## Overview

Infrastructure-as-Code management layer for Pi-hole. FastAPI backend that interacts with the Pi-hole API for analytics, dynamic blocklist management, and DNS reporting.

## Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Pi-hole API | HTTP (FTL) |
| Blocklist | Python + requests |
| Container | Docker compose |
| Analytics | Pi-hole API → JSON → reports |

## Data Flow

```
User ──> FastAPI ──> Pi-hole API ──> Analytics
  │                     │
  │                ┌────▼────┐
  │                │ Blocklist│
  │                │ Manager  │
  │                └─────────┘
  │
  └──> Healthcheck ──> docker-compose health
```

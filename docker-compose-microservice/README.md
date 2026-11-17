# Multi-Container Microservice with Docker Compose

Two services:
- **app-db**      – PostgreSQL 16 (seeded with sample data from `app-db/init.sql`)
- **app-service** – Python Flask API exposed on port 8080

## Prerequisites
Docker + Docker Compose (Docker Desktop, or Docker Engine with the compose plugin).

## Step 1 – Compose file
`docker-compose.yml` defines both services, env vars, network, volume and healthcheck.

## Step 2 – Deploy
```bash
docker-compose up -d --build      # or: docker compose up -d --build
docker-compose ps
```

## Step 3 – Test
```bash
curl http://localhost:8080/api/data
# or
./test.sh
```
Expected: JSON with `"status": "success"`, `"database": "connected"` and 3 records.

## Useful commands
```bash
docker-compose logs -f app-service
docker exec -it app-db psql -U appuser -d appdb -c "SELECT * FROM items;"
docker-compose down          # stop
docker-compose down -v       # stop + delete DB volume
```

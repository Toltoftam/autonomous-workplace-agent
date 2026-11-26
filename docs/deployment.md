# Deployment

## Local Development

```bash
docker-compose up --build
```

## Run Tests

```bash
pytest
```

## Security Scan

```bash
bandit -r src
```

## API

Health Endpoint

```bash
GET /health
```

Email Triage

```bash
POST /triage
```

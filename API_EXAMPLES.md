# API Examples

## Health
`GET /api/health`

## Stats
`GET /api/stats`

## Create event
`POST /api/events`

```json
{"event_type":"authentication","severity":"high","message":"Failed login burst","src_ip":"10.1.1.5","username":"admin","failed_logins":8}
```

## Train Isolation Forest
`POST /api/ml/train`

## Rebuild incidents
`POST /api/incidents/rebuild`

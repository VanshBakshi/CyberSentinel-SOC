def score_event(event, anomaly_score, hits):
    sev = {"critical": 100, "high": 75, "medium": 50, "low": 20}.get(str(event.severity).lower(), 20)
    failed = min(event.failed_logins * 4, 30)
    outbound = 20 if event.bytes_out >= 5_000_000 else (10 if event.bytes_out >= 1_000_000 else 0)
    rules = min(len(hits) * 12, 36)
    anomaly = min(max(anomaly_score, 0) * 25, 25)
    threat = min(100, sev * 0.45 + failed + outbound + rules)
    risk = min(100, threat * 0.65 + anomaly)
    return round(threat, 2), round(risk, 2)

def priority(score):
    if score >= 90: return "critical"
    if score >= 70: return "high"
    if score >= 40: return "medium"
    return "low"

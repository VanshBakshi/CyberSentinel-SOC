from collections import defaultdict
from datetime import timedelta
from hashlib import sha1
from app.db.models import Incident
from app.services.scoring import priority

def rebuild_incidents(db):
    events = db.query(__import__('app.db.models', fromlist=['Event']).Event).order_by(__import__('app.db.models', fromlist=['Event']).Event.timestamp.asc()).all()
    groups = defaultdict(list)
    for e in events:
        key = e.src_ip or e.username or e.hostname or "unknown"
        groups[key].append(e)
    db.query(Incident).delete()
    created = 0
    for key, items in groups.items():
        items = [e for e in items if e.risk_score >= 40 or e.rule_hits]
        if not items: continue
        buckets = []
        current = []
        for e in items:
            if current and e.timestamp - current[-1].timestamp > timedelta(minutes=20):
                buckets.append(current); current=[]
            current.append(e)
        if current: buckets.append(current)
        for bucket in buckets:
            max_risk = max(e.risk_score for e in bucket)
            tactics = sorted({m.get("tactic") for e in bucket for m in (e.mitre or []) if m.get("tactic")})
            techniques = sorted({m.get("technique") for e in bucket for m in (e.mitre or []) if m.get("technique")})
            ident = sha1(f"{key}:{bucket[0].timestamp.isoformat()}".encode()).hexdigest()[:16]
            timeline = [{"event_id": e.id, "time": e.timestamp.isoformat(), "type": e.event_type, "risk": e.risk_score, "message": e.message[:180]} for e in bucket]
            inc = Incident(incident_key=ident, title=f"Correlated activity from {key}", status="new", priority=priority(max_risk), risk_score=max_risk, source=key, username=bucket[0].username, event_count=len(bucket), first_seen=bucket[0].timestamp, last_seen=bucket[-1].timestamp, tactics=tactics, techniques=techniques, timeline=timeline)
            db.add(inc); created += 1
    db.commit(); return created

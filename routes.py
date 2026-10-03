import csv, io
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Event, Incident
from app.schemas import EventCreate, EventOut, IncidentUpdate
from app.services.detection import analyze
from app.services.ml_engine import engine
from app.services.scoring import priority, score_event
from app.services.correlation import rebuild_incidents
from app.services.elasticsearch_store import store
from app.services.torch_model import train_autoencoder

router = APIRouter(prefix="/api")

def process(payload, db):
    e = Event(timestamp=payload.timestamp or datetime.now(timezone.utc), event_type=payload.event_type, severity=payload.severity, message=payload.message, src_ip=payload.src_ip, dst_ip=payload.dst_ip, username=payload.username, hostname=payload.hostname, failed_logins=payload.failed_logins, bytes_in=payload.bytes_in, bytes_out=payload.bytes_out, raw=payload.raw)
    db.add(e); db.flush()
    hits, mitre, iocs = analyze(e); e.rule_hits=hits; e.mitre=mitre; e.iocs=iocs
    e.threat_score, e.risk_score = score_event(e, 0, hits)
    e.anomaly_score = round(engine.score(e), 4)
    e.threat_score, e.risk_score = score_event(e, e.anomaly_score, hits)
    db.commit(); db.refresh(e); store.index(e); return e

@router.get("/health")
def health(): return {"status":"ok","service":"CyberSentinel SOC"}

@router.get("/stats")
def stats(db: Session=Depends(get_db)):
    events=db.query(Event).count(); incidents=db.query(Incident).count()
    critical=db.query(Incident).filter(Incident.priority=="critical").count(); high=db.query(Incident).filter(Incident.priority=="high").count()
    avg=db.query(Event).all(); avg_risk=round(sum(e.risk_score for e in avg)/len(avg),2) if avg else 0
    return {"events":events,"incidents":incidents,"critical":critical,"high":high,"avg_risk":avg_risk}

@router.post("/events", response_model=EventOut)
def create_event(payload: EventCreate, db: Session=Depends(get_db)): return process(payload, db)

@router.post("/events/bulk")
def bulk(payload: list[EventCreate], db: Session=Depends(get_db)):
    created=[process(x,db) for x in payload]; return {"created":len(created),"ids":[x.id for x in created]}

@router.post("/events/upload")
async def upload(file: UploadFile=File(...), db: Session=Depends(get_db)):
    raw=(await file.read()).decode("utf-8-sig"); created=0
    if file.filename.lower().endswith(".csv"):
        rows=csv.DictReader(io.StringIO(raw))
    else:
        import json
        obj=json.loads(raw); rows=obj if isinstance(obj,list) else obj.get("events",[])
    for row in rows:
        def num(v, cast=float):
            try:return cast(v or 0)
            except:return cast(0)
        process(EventCreate(event_type=row.get("event_type","unknown"), severity=row.get("severity","low"), message=row.get("message","") or "", src_ip=row.get("src_ip"), dst_ip=row.get("dst_ip"), username=row.get("username"), hostname=row.get("hostname"), failed_logins=num(row.get("failed_logins"),int), bytes_in=num(row.get("bytes_in")), bytes_out=num(row.get("bytes_out"))), db); created+=1
    return {"created":created}

@router.get("/events")
def events(limit:int=100, q:str="", db:Session=Depends(get_db)):
    query=db.query(Event).order_by(Event.timestamp.desc())
    if q:
        from sqlalchemy import or_
        like=f"%{q}%"; query=query.filter(or_(Event.message.ilike(like),Event.src_ip.ilike(like),Event.username.ilike(like),Event.event_type.ilike(like)))
    return query.limit(min(limit,500)).all()

@router.get("/events/{event_id}")
def event(event_id:int, db:Session=Depends(get_db)):
    e=db.get(Event,event_id)
    if not e: raise HTTPException(404,"Event not found")
    return e

@router.post("/ml/train")
def train(db:Session=Depends(get_db)):
    events=db.query(Event).all(); n=engine.train(events); return {"status":"trained","samples":n}

@router.post("/ml/train-autoencoder")
def train_torch(db:Session=Depends(get_db)): return train_autoencoder(db.query(Event).all())

@router.post("/incidents/rebuild")
def rebuild(db:Session=Depends(get_db)): return {"created":rebuild_incidents(db)}

@router.get("/incidents")
def incidents(limit:int=100, status:str="", db:Session=Depends(get_db)):
    q=db.query(Incident).order_by(Incident.risk_score.desc())
    if status:q=q.filter(Incident.status==status)
    return q.limit(min(limit,500)).all()

@router.get("/incidents/{incident_id}")
def incident(incident_id:int, db:Session=Depends(get_db)):
    x=db.get(Incident,incident_id)
    if not x: raise HTTPException(404,"Incident not found")
    return x

@router.patch("/incidents/{incident_id}")
def update_incident(incident_id:int, payload:IncidentUpdate, db:Session=Depends(get_db)):
    x=db.get(Incident,incident_id)
    if not x: raise HTTPException(404,"Incident not found")
    if payload.status is not None:x.status=payload.status
    if payload.priority is not None:x.priority=payload.priority
    if payload.notes is not None:x.notes=payload.notes
    db.commit(); db.refresh(x); return x

@router.get("/search")
def search(q:str, db:Session=Depends(get_db)):
    return events(limit=100,q=q,db=db)

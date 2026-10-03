from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Float, Integer, String, Text, JSON
from app.db.database import Base

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), index=True)
    event_type = Column(String(80), index=True)
    severity = Column(String(30), default="low", index=True)
    message = Column(Text, default="")
    src_ip = Column(String(64), index=True)
    dst_ip = Column(String(64))
    username = Column(String(160), index=True)
    hostname = Column(String(160), index=True)
    failed_logins = Column(Integer, default=0)
    bytes_in = Column(Float, default=0)
    bytes_out = Column(Float, default=0)
    threat_score = Column(Float, default=0)
    anomaly_score = Column(Float, default=0)
    risk_score = Column(Float, default=0)
    rule_hits = Column(JSON, default=list)
    iocs = Column(JSON, default=dict)
    mitre = Column(JSON, default=list)
    raw = Column(JSON, default=dict)

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True)
    incident_key = Column(String(80), unique=True, index=True)
    title = Column(String(240))
    status = Column(String(40), default="new", index=True)
    priority = Column(String(30), default="medium", index=True)
    risk_score = Column(Float, default=0)
    source = Column(String(160))
    username = Column(String(160))
    event_count = Column(Integer, default=0)
    first_seen = Column(DateTime)
    last_seen = Column(DateTime)
    tactics = Column(JSON, default=list)
    techniques = Column(JSON, default=list)
    timeline = Column(JSON, default=list)
    notes = Column(Text, default="")

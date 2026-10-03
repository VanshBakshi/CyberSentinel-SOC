from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field, ConfigDict

class EventCreate(BaseModel):
    timestamp: Optional[datetime] = None
    event_type: str = "unknown"
    severity: str = "low"
    message: str = ""
    src_ip: Optional[str] = None
    dst_ip: Optional[str] = None
    username: Optional[str] = None
    hostname: Optional[str] = None
    failed_logins: int = 0
    bytes_in: float = 0
    bytes_out: float = 0
    raw: dict[str, Any] = Field(default_factory=dict)

class IncidentUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    notes: Optional[str] = None

class EventOut(EventCreate):
    id: int
    threat_score: float
    anomaly_score: float
    risk_score: float
    rule_hits: list[Any]
    iocs: dict[str, Any]
    mitre: list[Any]
    model_config = ConfigDict(from_attributes=True)

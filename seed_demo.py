from datetime import datetime, timedelta, timezone
import random
from app.db.database import Base, engine, SessionLocal
from app.db.models import Event
from app.schemas import EventCreate
from app.api.routes import process
from app.services.correlation import rebuild_incidents
from app.services.ml_engine import engine as ml

Base.metadata.create_all(bind=engine)
db=SessionLocal()
if db.query(Event).count()==0:
    random.seed(42); now=datetime.now(timezone.utc); rows=[]
    for i in range(150):
        rows.append(EventCreate(timestamp=now-timedelta(minutes=random.randint(0,720)), event_type=random.choice(["authentication","web","dns","process","network"]), severity=random.choice(["low","low","medium","medium","high"]), message=random.choice(["Normal application activity","Web request completed","DNS lookup","User login successful","Scheduled process executed"]), src_ip=f"10.0.{random.randint(1,20)}.{random.randint(2,240)}", username=random.choice(["analyst","user01","svc_web","admin"]), hostname=f"WS-{random.randint(1,40):03}", failed_logins=random.choice([0,0,0,1,2]), bytes_in=random.randint(100,100000), bytes_out=random.randint(100,500000)))
    for i in range(12):
        rows.append(EventCreate(timestamp=now-timedelta(minutes=i*3),event_type="authentication",severity="high",message="Multiple failed login attempts followed by credential access",src_ip="185.199.88.42",username="admin",hostname="DC-01",failed_logins=9+i%4,bytes_out=5000))
    for i in range(8):
        rows.append(EventCreate(timestamp=now-timedelta(minutes=i*2),event_type="port_scan",severity="high",message="Network port scan from suspicious source 185.199.88.42",src_ip="185.199.88.42",username="",hostname="FW-01",failed_logins=0,bytes_out=2000))
    for i in range(5):
        rows.append(EventCreate(timestamp=now-timedelta(minutes=i),event_type="process",severity="critical",message="PowerShell encoded command and ransomware behavior detected",src_ip="10.0.9.15",username="svc_web",hostname="APP-07",failed_logins=0,bytes_out=15_000_000))
    for r in rows: process(r,db)
    try: ml.train(db.query(Event).all())
    except Exception: pass
rebuild_incidents(db); print(f"Demo ready: {db.query(Event).count()} events, {__import__('app.db.models',fromlist=['Incident']).Incident.__tablename__} rebuilt")
db.close()

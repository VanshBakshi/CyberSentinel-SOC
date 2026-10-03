from types import SimpleNamespace
from app.services.scoring import score_event, priority

def test_high_risk():
    e=SimpleNamespace(severity="critical",failed_logins=10,bytes_out=8_000_000)
    threat,risk=score_event(e,1.0,["AUTH-BRUTEFORCE","EXFILTRATION"])
    assert threat>70 and risk>50

def test_priority():
    assert priority(95)=="critical"
    assert priority(75)=="high"
    assert priority(50)=="medium"

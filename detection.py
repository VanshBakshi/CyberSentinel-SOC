import re

RULES = [
    ("AUTH-BRUTEFORCE", "Credential Access", "T1110", lambda e: e.failed_logins >= 5),
    ("NETWORK-SCAN", "Discovery", "T1046", lambda e: e.event_type.lower() in {"port_scan", "scan", "network_scan"}),
    ("POWERSHELL", "Execution", "T1059.001", lambda e: "powershell" in e.message.lower()),
    ("CREDENTIAL", "Credential Access", "T1003", lambda e: any(x in e.message.lower() for x in ["credential", "mimikatz", "lsass"])),
    ("MALWARE", "Impact", "T1486", lambda e: any(x in e.message.lower() for x in ["malware", "ransomware", "encrypt files"])),
    ("EXFILTRATION", "Exfiltration", "T1041", lambda e: e.bytes_out >= 5_000_000),
]

def analyze(event):
    hits, mitre = [], []
    for name, tactic, technique, fn in RULES:
        try:
            if fn(event):
                hits.append(name); mitre.append({"tactic": tactic, "technique": technique})
        except Exception:
            pass
    ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", event.message or "")
    domains = re.findall(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b", event.message or "")
    hashes = re.findall(r"\b[a-fA-F0-9]{32,64}\b", event.message or "")
    return hits, mitre, {"ips": ips, "domains": domains, "hashes": hashes}

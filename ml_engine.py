from pathlib import Path
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest

MODEL_PATH = Path("models/isolation_forest.joblib")
FEATURES = ["bytes_in", "bytes_out", "failed_logins", "threat_score", "message_length", "is_external"]

class AnomalyEngine:
    def __init__(self):
        self.model = joblib.load(MODEL_PATH) if MODEL_PATH.exists() else None

    def vector(self, e):
        return [float(e.bytes_in or 0), float(e.bytes_out or 0), float(e.failed_logins or 0), float(e.threat_score or 0), float(len(e.message or "")), 1.0 if e.src_ip else 0.0]

    def score(self, e):
        if not self.model:
            return min(1.0, (e.failed_logins or 0)/20 + (e.bytes_out or 0)/20_000_000 + (e.threat_score or 0)/250)
        raw = self.model.decision_function([self.vector(e)])[0]
        return float(np.clip(0.5 - raw, 0, 1))

    def train(self, events):
        if len(events) < 10:
            raise ValueError("At least 10 events are required to train the anomaly model")
        X = np.array([self.vector(e) for e in events], dtype=float)
        self.model = IsolationForest(n_estimators=250, contamination=0.08, random_state=42, n_jobs=-1)
        self.model.fit(X)
        MODEL_PATH.parent.mkdir(exist_ok=True)
        joblib.dump(self.model, MODEL_PATH)
        return len(events)

engine = AnomalyEngine()

from app.core.config import settings
class ElasticStore:
    def __init__(self):
        self.client = None
        if settings.elasticsearch_enabled:
            try:
                from elasticsearch import Elasticsearch
                self.client = Elasticsearch(settings.elasticsearch_url)
            except Exception:
                self.client = None
    def index(self, event):
        if not self.client: return False
        try:
            self.client.index(index=settings.elasticsearch_index, id=str(event.id), document={"id": event.id, "timestamp": event.timestamp.isoformat(), "event_type": event.event_type, "message": event.message, "src_ip": event.src_ip, "username": event.username, "risk_score": event.risk_score, "rule_hits": event.rule_hits})
            return True
        except Exception:
            return False
store = ElasticStore()

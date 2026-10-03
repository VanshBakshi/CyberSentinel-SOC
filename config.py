from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "CyberSentinel SOC"
    database_url: str = "sqlite:///./cybersentinel.db"
    elasticsearch_enabled: bool = False
    elasticsearch_url: str = "http://localhost:9200"
    elasticsearch_index: str = "cybersentinel-events"
    anomaly_contamination: float = 0.08
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

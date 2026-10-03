from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.logging import configure_logging
from app.db.database import Base, engine
from app.api.routes import router

configure_logging(); Base.metadata.create_all(bind=engine)
app=FastAPI(title=settings.app_name, version="1.0.0", description="SOC alert correlation, anomaly detection and incident prioritization platform")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"])
app.include_router(router)
frontend=Path(__file__).resolve().parent.parent/"frontend"
app.mount("/", StaticFiles(directory=str(frontend), html=True), name="frontend")

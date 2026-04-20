from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.core.database import MongoDB
from app.core.middleware import register_middleware

app = FastAPI(title=settings.app_name)
register_middleware(app)

@app.on_event("startup")
async def startup_event():
    await MongoDB.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await MongoDB.close()

@app.get("/")
async def root():
    return {"service": settings.app_name, "status": "ok"}

@app.get("/health/db")
async def db_health():
    try:
        await MongoDB.client.admin.command("ping")
        return {"database": "connected"}
    except Exception as exc:
        return {"database": "failed", "error": str(exc)}

app.include_router(api_router, prefix=settings.api_v1_prefix)

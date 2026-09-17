from fastapi import FastAPI
from app.api.evaluations import router as evaluations_router
from app.core.config import settings

print(settings.environment)

app = FastAPI(
    title="AI Evaluation API",
    version="0.1.0",
)

app.include_router(evaluations_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}

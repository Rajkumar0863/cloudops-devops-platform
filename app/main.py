from fastapi import FastAPI

app = FastAPI(
    title="CloudOps API",
    description="API service for the CloudOps DevOps platform project",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "CloudOps API",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def readiness():
    return {
        "status": "ready"
    }
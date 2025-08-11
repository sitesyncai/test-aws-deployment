from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
from datetime import datetime

app = FastAPI(
    title="AWS App Runner FastAPI Demo",
    description="A simple FastAPI application for AWS App Runner deployment",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageResponse(BaseModel):
    message: str
    timestamp: str
    environment: str

@app.get("/")
async def root():
    """Root endpoint returning hello world message"""
    return MessageResponse(
        message="Hello World from FastAPI on AWS App Runner!",
        timestamp=datetime.now().isoformat(),
        environment=os.getenv("ENVIRONMENT", "local")
    )

@app.get("/health")
async def health_check():
    """Health check endpoint for AWS App Runner"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/info")
async def get_info():
    """Get application information"""
    return {
        "app_name": "FastAPI AWS Demo",
        "version": "1.0.0",
        "python_version": "3.11",
        "environment": os.getenv("ENVIRONMENT", "local"),
        "port": os.getenv("PORT", "8000")
    }

@app.post("/api/echo")
async def echo_message(message: dict):
    """Echo back the received message with timestamp"""
    return {
        "received": message,
        "echoed_at": datetime.now().isoformat(),
        "server": "FastAPI on AWS App Runner"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        access_log=True
    )

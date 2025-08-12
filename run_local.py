#!/usr/bin/env python3
"""
Local development server script for FastAPI application
Run this script to start the development server with hot reload
"""

import uvicorn
import os
print("this is to check if the file is running")
print(__name__)
if __name__ == "__main__":
    
    # Set development environment
    os.environ["ENVIRONMENT"] = "development"
    
    print("🚀 Starting FastAPI development server...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API documentation at: http://localhost:8000/docs")
    print("🔧 ReDoc documentation at: http://localhost:8000/redoc")
    print("❤️  Health check at: http://localhost:8000/health")
    print("\n⚡ Hot reload is enabled - changes will auto-restart the server")
    print("🛑 Press Ctrl+C to stop the server\n")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        reload_dirs=["./"],
        log_level="info"
    )

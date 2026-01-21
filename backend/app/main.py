"""
EduPredict AI - Main FastAPI Application
Production-ready backend with modern architecture
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
import time
from typing import Dict, Any
import logging

from app.core.config import settings
from app.api import prediction, users, analytics, health

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="""
    🎓 EduPredict AI - Student Success Prediction Platform
    
    ## Features
    * **Admission Prediction**: ML-powered university admission probability
    * **Dropout Risk Assessment**: Early identification of at-risk students
    * **Explainable AI**: SHAP-based feature importance
    * **Personalized Recommendations**: AI-driven student guidance
    * **Real-time Analytics**: Dashboard with actionable insights
    
    ## Tech Stack
    * FastAPI (async Python web framework)
    * XGBoost & scikit-learn (ML models)
    * PostgreSQL (primary database)
    * Redis (caching layer)
    * SHAP (explainable AI)
    """,
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"{request.method} {request.url.path} - {process_time:.3f}s")
    return response

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["Health"])
app.include_router(prediction.router, prefix="/api/v1/predictions", tags=["Predictions"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logger.info("🚀 Starting EduPredict AI Backend...")
    logger.info(f"📝 Environment: {settings.ENVIRONMENT}")
    logger.info(f"📊 API Documentation: {settings.API_URL}/docs")

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    logger.info("👋 Shutting down EduPredict AI Backend...")

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "🎓 Welcome to EduPredict AI",
        "description": "Student Success Prediction Platform",
        "version": settings.VERSION,
        "docs": f"{settings.API_URL}/docs",
        "health": f"{settings.API_URL}/api/v1/health",
        "features": [
            "Admission Prediction",
            "Dropout Risk Assessment",
            "Explainable AI",
            "Personalized Recommendations",
            "Real-time Analytics"
        ]
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "path": str(request.url)
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """General exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred"
        }
    )

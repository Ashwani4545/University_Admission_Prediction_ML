"""Schemas module initialization"""
from app.schemas.predictions import (
    AdmissionPredictionRequest,
    AdmissionPredictionResponse,
    DropoutPredictionRequest,
    DropoutPredictionResponse,
    HybridPredictionRequest,
    HybridPredictionResponse,
    ErrorResponse
)

__all__ = [
    "AdmissionPredictionRequest",
    "AdmissionPredictionResponse",
    "DropoutPredictionRequest",
    "DropoutPredictionResponse",
    "HybridPredictionRequest",
    "HybridPredictionResponse",
    "ErrorResponse"
]

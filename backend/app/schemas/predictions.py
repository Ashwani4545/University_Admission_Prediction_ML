"""
Pydantic Schemas for Request/Response Validation
"""
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

# Enums
class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class EducationLevel(str, Enum):
    HIGH_SCHOOL = "high_school"
    BACHELORS = "bachelors"
    MASTERS = "masters"
    PHD = "phd"

class SocioEconomicStatus(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

# Admission Prediction Schemas
class AdmissionPredictionRequest(BaseModel):
    """Request schema for admission prediction"""
    gre_score: int = Field(..., ge=260, le=340, description="GRE exam score (260-340)")
    toefl_score: int = Field(..., ge=0, le=120, description="TOEFL exam score (0-120)")
    university_rating: int = Field(..., ge=1, le=5, description="University rating (1-5)")
    sop_strength: float = Field(..., ge=1.0, le=5.0, description="Statement of Purpose strength (1-5)")
    lor_strength: float = Field(..., ge=1.0, le=5.0, description="Letter of Recommendation strength (1-5)")
    cgpa: float = Field(..., ge=0.0, le=10.0, description="Undergraduate CGPA (0-10)")
    research_experience: bool = Field(..., description="Has research experience")
    
    class Config:
        json_schema_extra = {
            "example": {
                "gre_score": 320,
                "toefl_score": 110,
                "university_rating": 4,
                "sop_strength": 4.5,
                "lor_strength": 4.0,
                "cgpa": 8.5,
                "research_experience": True
            }
        }

# Dropout Prediction Schemas
class DropoutPredictionRequest(BaseModel):
    """Request schema for dropout risk prediction"""
    age: int = Field(..., ge=15, le=30, description="Student age")
    gender: Gender = Field(..., description="Student gender")
    parent_education: EducationLevel = Field(..., description="Highest parent education level")
    socio_economic_status: SocioEconomicStatus = Field(..., description="Family socio-economic status")
    attendance_rate: float = Field(..., ge=0.0, le=100.0, description="Attendance percentage")
    academic_grades: float = Field(..., ge=0.0, le=100.0, description="Average academic grades")
    family_support: bool = Field(..., description="Has family support")
    distance_from_school: float = Field(..., ge=0.0, le=100.0, description="Distance in kilometers")
    study_hours: float = Field(..., ge=0.0, le=24.0, description="Daily study hours")
    
    class Config:
        json_schema_extra = {
            "example": {
                "age": 18,
                "gender": "male",
                "parent_education": "bachelors",
                "socio_economic_status": "medium",
                "attendance_rate": 85.5,
                "academic_grades": 75.0,
                "family_support": True,
                "distance_from_school": 5.0,
                "study_hours": 4.0
            }
        }

# Feature Importance Schema
class FeatureImportance(BaseModel):
    """Feature importance with explanation"""
    feature: str = Field(..., description="Feature name")
    importance: float = Field(..., description="Importance score")
    impact: str = Field(..., description="Impact direction (positive/negative)")
    explanation: str = Field(..., description="Human-readable explanation")

# Recommendation Schema
class Recommendation(BaseModel):
    """Personalized recommendation"""
    category: str = Field(..., description="Recommendation category")
    title: str = Field(..., description="Recommendation title")
    description: str = Field(..., description="Detailed description")
    priority: str = Field(..., description="Priority level (high/medium/low)")
    actionable_steps: List[str] = Field(..., description="Specific action items")

# Admission Prediction Response
class AdmissionPredictionResponse(BaseModel):
    """Response schema for admission prediction"""
    prediction_id: str = Field(..., description="Unique prediction ID")
    admission_probability: float = Field(..., ge=0.0, le=1.0, description="Probability of admission")
    admission_percentage: float = Field(..., ge=0.0, le=100.0, description="Admission chance percentage")
    confidence_level: str = Field(..., description="Model confidence (high/medium/low)")
    risk_level: RiskLevel = Field(..., description="Overall risk assessment")
    feature_importance: List[FeatureImportance] = Field(..., description="Top features affecting prediction")
    recommendations: List[Recommendation] = Field(..., description="Personalized recommendations")
    similar_profiles: Optional[Dict[str, Any]] = Field(None, description="Similar successful profiles")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Prediction timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction_id": "pred_abc123",
                "admission_probability": 0.78,
                "admission_percentage": 78.0,
                "confidence_level": "high",
                "risk_level": "low",
                "feature_importance": [
                    {
                        "feature": "CGPA",
                        "importance": 0.35,
                        "impact": "positive",
                        "explanation": "Your CGPA of 8.5 significantly increases your chances"
                    }
                ],
                "recommendations": [
                    {
                        "category": "Test Preparation",
                        "title": "Improve GRE Score",
                        "description": "Consider retaking GRE to improve from 320 to 325+",
                        "priority": "medium",
                        "actionable_steps": [
                            "Enroll in GRE prep course",
                            "Practice 2 hours daily for 2 months"
                        ]
                    }
                ],
                "timestamp": "2024-01-21T10:30:00Z"
            }
        }

# Dropout Prediction Response
class DropoutPredictionResponse(BaseModel):
    """Response schema for dropout risk prediction"""
    prediction_id: str = Field(..., description="Unique prediction ID")
    dropout_risk: bool = Field(..., description="Whether student is at dropout risk")
    dropout_probability: float = Field(..., ge=0.0, le=1.0, description="Probability of dropping out")
    dropout_percentage: float = Field(..., ge=0.0, le=100.0, description="Dropout risk percentage")
    risk_level: RiskLevel = Field(..., description="Risk level classification")
    confidence_level: str = Field(..., description="Model confidence")
    feature_importance: List[FeatureImportance] = Field(..., description="Key risk factors")
    recommendations: List[Recommendation] = Field(..., description="Intervention recommendations")
    early_warning_indicators: List[str] = Field(..., description="Warning signs to monitor")
    support_resources: List[Dict[str, str]] = Field(..., description="Available support services")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Prediction timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction_id": "pred_xyz789",
                "dropout_risk": False,
                "dropout_probability": 0.25,
                "dropout_percentage": 25.0,
                "risk_level": "low",
                "confidence_level": "high",
                "feature_importance": [
                    {
                        "feature": "Attendance Rate",
                        "importance": 0.28,
                        "impact": "positive",
                        "explanation": "Your 85% attendance rate is healthy"
                    }
                ],
                "recommendations": [
                    {
                        "category": "Academic Support",
                        "title": "Maintain Current Performance",
                        "description": "Continue your current study habits",
                        "priority": "low",
                        "actionable_steps": [
                            "Keep attending classes regularly",
                            "Maintain study routine"
                        ]
                    }
                ],
                "early_warning_indicators": [
                    "Sudden drop in attendance",
                    "Decline in grades"
                ],
                "support_resources": [
                    {
                        "name": "Academic Counseling",
                        "description": "One-on-one academic support",
                        "contact": "counseling@university.edu"
                    }
                ],
                "timestamp": "2024-01-21T10:30:00Z"
            }
        }

# Combined Prediction Schema
class HybridPredictionRequest(BaseModel):
    """Combined admission and dropout prediction request"""
    admission_data: AdmissionPredictionRequest
    dropout_data: Optional[DropoutPredictionRequest] = None

class HybridPredictionResponse(BaseModel):
    """Combined prediction response"""
    admission_prediction: AdmissionPredictionResponse
    dropout_prediction: Optional[DropoutPredictionResponse] = None
    overall_assessment: Dict[str, Any] = Field(..., description="Holistic student assessment")
    success_score: float = Field(..., ge=0.0, le=100.0, description="Overall success probability score")

# Error Response Schema
class ErrorResponse(BaseModel):
    """Standard error response"""
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(None, description="Detailed error information")
    status_code: int = Field(..., description="HTTP status code")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

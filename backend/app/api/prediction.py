"""
Prediction API Endpoints
Handles admission and dropout predictions with explainable AI
"""
from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import Dict, Any
import uuid
import logging

from app.schemas.predictions import (
    AdmissionPredictionRequest,
    AdmissionPredictionResponse,
    DropoutPredictionRequest,
    DropoutPredictionResponse,
    FeatureImportance,
    Recommendation,
    RiskLevel
)
from app.ml.admission_model import AdmissionPredictor
from app.ml.dropout_model import DropoutPredictor
from app.services.recommendation_engine import RecommendationEngine

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize ML models (singleton pattern)
admission_predictor = AdmissionPredictor()
dropout_predictor = DropoutPredictor()
recommendation_engine = RecommendationEngine()

@router.post("/admission", response_model=AdmissionPredictionResponse)
async def predict_admission(request: AdmissionPredictionRequest):
    """
    Predict university admission probability
    
    This endpoint uses ensemble machine learning models to predict
    the probability of university admission based on academic metrics.
    
    **Features:**
    - ML-powered prediction using Linear Regression
    - Feature importance analysis
    - Personalized recommendations
    - Confidence scoring
    
    **Returns:**
    - Admission probability (0-1)
    - Risk level assessment
    - Top factors affecting admission
    - Actionable recommendations
    """
    try:
        logger.info(f"Processing admission prediction request")
        
        # Convert request to dict
        features = request.model_dump()
        
        # Get prediction
        probability, metadata = admission_predictor.predict(features)
        
        # Generate unique prediction ID
        prediction_id = f"adm_{uuid.uuid4().hex[:12]}"
        
        # Calculate risk level
        risk_level = _calculate_admission_risk_level(probability)
        
        # Generate feature importance explanations
        feature_importance = _generate_feature_importance(
            metadata['feature_importance'],
            features,
            'admission'
        )
        
        # Generate recommendations
        recommendations = recommendation_engine.generate_admission_recommendations(
            features,
            probability,
            feature_importance
        )
        
        # Build response
        response = AdmissionPredictionResponse(
            prediction_id=prediction_id,
            admission_probability=probability,
            admission_percentage=round(probability * 100, 2),
            confidence_level=metadata['confidence'],
            risk_level=risk_level,
            feature_importance=feature_importance[:5],  # Top 5
            recommendations=recommendations,
            similar_profiles={
                "count": 150,
                "avg_admission_rate": 0.75,
                "recommendation": "Students with similar profiles have 75% admission rate"
            }
        )
        
        logger.info(f"Admission prediction completed: {prediction_id} - {probability:.2%}")
        return response
        
    except Exception as e:
        logger.error(f"Error in admission prediction: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@router.post("/dropout", response_model=DropoutPredictionResponse)
async def predict_dropout(request: DropoutPredictionRequest):
    """
    Predict student dropout risk
    
    This endpoint uses classification models to assess the risk
    of a student dropping out based on various factors.
    
    **Features:**
    - Random Forest classification
    - Risk factor identification
    - Early warning indicators
    - Intervention recommendations
    
    **Returns:**
    - Dropout probability
    - Risk level (low/medium/high/critical)
    - Key risk factors
    - Support resources
    """
    try:
        logger.info(f"Processing dropout prediction request")
        
        # Convert request to dict
        features = request.model_dump()
        
        # Get prediction
        dropout_risk, probability, metadata = dropout_predictor.predict(features)
        
        # Generate unique prediction ID
        prediction_id = f"dro_{uuid.uuid4().hex[:12]}"
        
        # Calculate risk level
        risk_level = _calculate_dropout_risk_level(probability)
        
        # Generate feature importance explanations
        feature_importance = _generate_feature_importance(
            metadata['feature_importance'],
            features,
            'dropout'
        )
        
        # Generate recommendations
        recommendations = recommendation_engine.generate_dropout_recommendations(
            features,
            dropout_risk,
            probability,
            metadata.get('risk_factors', [])
        )
        
        # Generate early warning indicators
        early_warnings = _generate_early_warnings(features, dropout_risk)
        
        # Generate support resources
        support_resources = _generate_support_resources(risk_level)
        
        # Build response
        response = DropoutPredictionResponse(
            prediction_id=prediction_id,
            dropout_risk=dropout_risk,
            dropout_probability=probability,
            dropout_percentage=round(probability * 100, 2),
            risk_level=risk_level,
            confidence_level=metadata['confidence'],
            feature_importance=feature_importance[:5],  # Top 5
            recommendations=recommendations,
            early_warning_indicators=early_warnings,
            support_resources=support_resources
        )
        
        logger.info(f"Dropout prediction completed: {prediction_id} - Risk: {risk_level}")
        return response
        
    except Exception as e:
        logger.error(f"Error in dropout prediction: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

def _calculate_admission_risk_level(probability: float) -> RiskLevel:
    """Calculate risk level for admission probability"""
    if probability >= 0.7:
        return RiskLevel.LOW  # High admission chance = low risk
    elif probability >= 0.5:
        return RiskLevel.MEDIUM
    elif probability >= 0.3:
        return RiskLevel.HIGH
    else:
        return RiskLevel.CRITICAL

def _calculate_dropout_risk_level(probability: float) -> RiskLevel:
    """Calculate risk level for dropout probability"""
    if probability < 0.25:
        return RiskLevel.LOW
    elif probability < 0.5:
        return RiskLevel.MEDIUM
    elif probability < 0.75:
        return RiskLevel.HIGH
    else:
        return RiskLevel.CRITICAL

def _generate_feature_importance(
    importance_dict: Dict[str, float],
    features: Dict[str, Any],
    prediction_type: str
) -> list[FeatureImportance]:
    """Generate feature importance with explanations"""
    feature_list = []
    
    # Sort by importance
    sorted_features = sorted(
        importance_dict.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    for feature_name, importance_score in sorted_features:
        # Get feature value
        feature_value = features.get(feature_name)
        
        # Generate explanation
        explanation = _generate_feature_explanation(
            feature_name,
            feature_value,
            importance_score,
            prediction_type
        )
        
        # Determine impact
        impact = _determine_feature_impact(feature_name, feature_value, prediction_type)
        
        feature_list.append(FeatureImportance(
            feature=_format_feature_name(feature_name),
            importance=round(importance_score, 3),
            impact=impact,
            explanation=explanation
        ))
    
    return feature_list

def _format_feature_name(name: str) -> str:
    """Format feature name for display"""
    return name.replace('_', ' ').title()

def _determine_feature_impact(feature_name: str, value: Any, prediction_type: str) -> str:
    """Determine if feature has positive or negative impact"""
    if prediction_type == 'admission':
        # For admission, higher values are generally positive
        positive_features = ['gre_score', 'toefl_score', 'cgpa', 'research_experience']
        return 'positive' if feature_name in positive_features and value else 'neutral'
    else:
        # For dropout, lower values are generally positive
        negative_features = ['attendance_rate', 'academic_grades', 'family_support', 'study_hours']
        return 'positive' if feature_name in negative_features else 'negative'

def _generate_feature_explanation(
    feature_name: str,
    value: Any,
    importance: float,
    prediction_type: str
) -> str:
    """Generate human-readable explanation for feature"""
    explanations = {
        'admission': {
            'gre_score': f"Your GRE score of {value} significantly influences your admission chances",
            'toefl_score': f"TOEFL score of {value} affects your English proficiency assessment",
            'cgpa': f"Your CGPA of {value}/10 is a major factor in admission decisions",
            'university_rating': f"Applying to tier-{value} universities impacts your chances",
            'sop_strength': f"Your SOP strength of {value}/5 contributes to your application",
            'lor_strength': f"LOR strength of {value}/5 supports your application",
            'research_experience': f"Research experience {'strengthens' if value else 'is not present in'} your profile"
        },
        'dropout': {
            'attendance_rate': f"Your {value}% attendance rate is a key indicator",
            'academic_grades': f"Academic performance of {value}% significantly impacts risk",
            'family_support': f"Family support {'presence' if value else 'absence'} is important",
            'socio_economic_status': f"{value.upper()} socio-economic status influences dropout risk",
            'study_hours': f"{value} hours of daily study affects academic success",
            'distance_from_school': f"{value}km distance from school is a consideration",
            'parent_education': f"Parent education level ({value}) plays a role",
            'age': f"Age {value} is factored into the analysis",
            'gender': f"Demographic factors are considered"
        }
    }
    
    return explanations.get(prediction_type, {}).get(
        feature_name,
        f"{_format_feature_name(feature_name)} contributes {importance:.1%} to the prediction"
    )

def _generate_early_warnings(features: Dict[str, Any], dropout_risk: bool) -> list[str]:
    """Generate early warning indicators"""
    warnings = []
    
    if features['attendance_rate'] < 80:
        warnings.append("Attendance falling below 80% threshold")
    
    if features['academic_grades'] < 70:
        warnings.append("Academic performance below passing grade")
    
    if not features['family_support']:
        warnings.append("Lack of family support system")
    
    if features['study_hours'] < 2:
        warnings.append("Insufficient daily study time")
    
    if features['distance_from_school'] > 15:
        warnings.append("Long commute distance affecting engagement")
    
    # Add general warnings
    if dropout_risk:
        warnings.extend([
            "Sudden changes in behavior or engagement",
            "Declining participation in class activities",
            "Increased absences without explanation"
        ])
    
    return warnings[:5]  # Top 5 warnings

def _generate_support_resources(risk_level: RiskLevel) -> list[Dict[str, str]]:
    """Generate list of support resources based on risk level"""
    resources = [
        {
            "name": "Academic Counseling",
            "description": "One-on-one academic support and guidance",
            "contact": "counseling@university.edu",
            "availability": "Monday-Friday, 9 AM - 5 PM"
        },
        {
            "name": "Tutoring Center",
            "description": "Free tutoring for all subjects",
            "contact": "tutoring@university.edu",
            "availability": "Monday-Saturday, 10 AM - 8 PM"
        },
        {
            "name": "Financial Aid Office",
            "description": "Financial assistance and scholarship information",
            "contact": "finaid@university.edu",
            "availability": "Monday-Friday, 8 AM - 4 PM"
        }
    ]
    
    if risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
        resources.extend([
            {
                "name": "Mental Health Services",
                "description": "Confidential counseling and mental health support",
                "contact": "wellness@university.edu",
                "availability": "24/7 Crisis Line: 1-800-XXX-XXXX"
            },
            {
                "name": "Student Success Coach",
                "description": "Personalized success planning and intervention",
                "contact": "success@university.edu",
                "availability": "By appointment"
            }
        ])
    
    return resources

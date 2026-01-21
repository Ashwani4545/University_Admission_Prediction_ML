"""
Machine Learning Service - Dropout Prediction Model
Uses classification models to predict student dropout risk
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os
from typing import Dict, Any, Tuple, List
import logging

logger = logging.getLogger(__name__)

class DropoutPredictor:
    """
    Student Dropout Risk Prediction Model
    
    Uses Random Forest Classifier for dropout prediction
    with feature importance analysis.
    """
    
    def __init__(self, model_path: str = None):
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.is_trained = False
        self.model_path = model_path
        
        self.feature_names = [
            'age', 'gender', 'parent_education', 'socio_economic_status',
            'attendance_rate', 'academic_grades', 'family_support',
            'distance_from_school', 'study_hours'
        ]
        
        self.categorical_features = ['gender', 'parent_education', 'socio_economic_status']
        
        # Initialize label encoders
        for feature in self.categorical_features:
            self.label_encoders[feature] = LabelEncoder()
        
        # Try to load pre-trained model
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
    
    def predict(self, features: Dict[str, Any]) -> Tuple[bool, float, Dict[str, Any]]:
        """
        Predict dropout risk
        
        Args:
            features: Dictionary with student features
            
        Returns:
            Tuple of (dropout_risk, probability, metadata)
        """
        if not self.is_trained:
            logger.warning("Model not trained, using heuristic prediction")
            return self._heuristic_prediction(features)
        
        # Prepare input
        X = self._prepare_features(features)
        
        # Scale and predict
        X_scaled = self.scaler.transform([X])
        
        # Get prediction and probability
        prediction = bool(self.model.predict(X_scaled)[0])
        probabilities = self.model.predict_proba(X_scaled)[0]
        dropout_probability = float(probabilities[1])  # Probability of dropout
        
        # Get feature importance
        feature_importance = self._get_feature_importance()
        
        metadata = {
            'model_type': 'Random Forest Classifier',
            'confidence': self._calculate_confidence(dropout_probability),
            'feature_importance': feature_importance,
            'risk_factors': self._identify_risk_factors(features, feature_importance)
        }
        
        return prediction, dropout_probability, metadata
    
    def _prepare_features(self, features: Dict[str, Any]) -> List[float]:
        """Encode and prepare features for prediction"""
        encoded_features = []
        
        for feature_name in self.feature_names:
            value = features[feature_name]
            
            if feature_name in self.categorical_features:
                # Encode categorical features
                if not self.is_trained:
                    # Fit encoder if not trained
                    self.label_encoders[feature_name].fit([value])
                encoded_value = self.label_encoders[feature_name].transform([value])[0]
                encoded_features.append(float(encoded_value))
            elif feature_name == 'family_support':
                # Convert boolean to int
                encoded_features.append(float(1 if value else 0))
            else:
                # Numerical features
                encoded_features.append(float(value))
        
        return encoded_features
    
    def _heuristic_prediction(self, features: Dict[str, Any]) -> Tuple[bool, float, Dict[str, Any]]:
        """
        Heuristic-based prediction for demo purposes
        
        Uses rule-based logic to estimate dropout risk
        """
        risk_score = 0.0
        
        # Attendance is critical
        if features['attendance_rate'] < 75:
            risk_score += 0.3
        elif features['attendance_rate'] < 85:
            risk_score += 0.15
        
        # Academic performance
        if features['academic_grades'] < 60:
            risk_score += 0.25
        elif features['academic_grades'] < 70:
            risk_score += 0.10
        
        # Family support
        if not features['family_support']:
            risk_score += 0.15
        
        # Socio-economic status
        if features['socio_economic_status'] == 'low':
            risk_score += 0.10
        
        # Distance from school
        if features['distance_from_school'] > 20:
            risk_score += 0.10
        elif features['distance_from_school'] > 10:
            risk_score += 0.05
        
        # Study hours
        if features['study_hours'] < 2:
            risk_score += 0.10
        
        # Parent education
        if features['parent_education'] in ['high_school', None]:
            risk_score += 0.05
        
        risk_score = min(risk_score, 1.0)  # Cap at 1.0
        
        dropout_risk = risk_score > 0.5
        
        metadata = {
            'model_type': 'Heuristic Model (Demo)',
            'confidence': 'medium',
            'feature_importance': self._mock_feature_importance(),
            'risk_factors': self._identify_risk_factors(features, self._mock_feature_importance())
        }
        
        return dropout_risk, risk_score, metadata
    
    def _get_feature_importance(self) -> Dict[str, float]:
        """Get feature importance from trained model"""
        if not self.is_trained:
            return self._mock_feature_importance()
        
        importance = self.model.feature_importances_
        feature_importance = {}
        
        for i, name in enumerate(self.feature_names):
            feature_importance[name] = float(importance[i])
        
        return feature_importance
    
    def _mock_feature_importance(self) -> Dict[str, float]:
        """Generate mock feature importance for demo"""
        return {
            'attendance_rate': 0.28,
            'academic_grades': 0.25,
            'family_support': 0.15,
            'socio_economic_status': 0.12,
            'study_hours': 0.10,
            'distance_from_school': 0.06,
            'parent_education': 0.03,
            'age': 0.01,
            'gender': 0.00
        }
    
    def _identify_risk_factors(self, features: Dict[str, Any], importance: Dict[str, float]) -> List[Dict[str, Any]]:
        """Identify top risk factors for the student"""
        risk_factors = []
        
        # Analyze each feature
        if features['attendance_rate'] < 80:
            risk_factors.append({
                'factor': 'Low Attendance',
                'severity': 'high',
                'current_value': features['attendance_rate'],
                'recommendation': 'Improve attendance to above 85%'
            })
        
        if features['academic_grades'] < 70:
            risk_factors.append({
                'factor': 'Low Academic Performance',
                'severity': 'high',
                'current_value': features['academic_grades'],
                'recommendation': 'Seek tutoring support'
            })
        
        if not features['family_support']:
            risk_factors.append({
                'factor': 'Lack of Family Support',
                'severity': 'medium',
                'current_value': False,
                'recommendation': 'Connect with school counseling services'
            })
        
        if features['study_hours'] < 3:
            risk_factors.append({
                'factor': 'Insufficient Study Time',
                'severity': 'medium',
                'current_value': features['study_hours'],
                'recommendation': 'Increase daily study time to 3-4 hours'
            })
        
        return risk_factors[:3]  # Return top 3
    
    def _calculate_confidence(self, probability: float) -> str:
        """Determine confidence level based on probability"""
        if 0.3 <= probability <= 0.7:
            return 'medium'
        return 'high'
    
    def save_model(self, path: str):
        """Save trained model to disk"""
        if not self.is_trained:
            raise ValueError("Cannot save untrained model")
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'feature_names': self.feature_names
        }
        joblib.dump(model_data, path)
        logger.info(f"Model saved to {path}")
    
    def load_model(self, path: str):
        """Load trained model from disk"""
        model_data = joblib.load(path)
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.label_encoders = model_data['label_encoders']
        self.feature_names = model_data['feature_names']
        self.is_trained = True
        logger.info(f"Model loaded from {path}")

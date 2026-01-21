"""
Machine Learning Service - Admission Prediction Model
Uses ensemble methods with XGBoost and Linear Regression
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os
from typing import Dict, Any, Tuple
import logging

logger = logging.getLogger(__name__)

class AdmissionPredictor:
    """
    Admission Probability Prediction Model
    
    Combines Linear Regression with feature engineering for
    accurate university admission predictions.
    """
    
    def __init__(self, model_path: str = None):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.is_trained = False
        self.model_path = model_path
        self.feature_names = [
            'gre_score', 'toefl_score', 'university_rating',
            'sop_strength', 'lor_strength', 'cgpa', 'research_experience'
        ]
        
        # Try to load pre-trained model
        if model_path and os.path.exists(model_path):
            self.load_model(model_path)
    
    def train(self, data_path: str) -> Dict[str, float]:
        """
        Train the admission prediction model
        
        Args:
            data_path: Path to training data CSV
            
        Returns:
            Dictionary with training metrics
        """
        logger.info(f"Training admission model with data from {data_path}")
        
        # Load data
        df = pd.read_csv(data_path)
        
        # Prepare features and target (strip whitespace from column names)
        df.columns = df.columns.str.strip()
        X = df[self.feature_names].copy()
        y = df['Chance of Admit'].values
        
        # Convert research to binary
        X['research_experience'] = X['research_experience'].astype(int)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model.fit(X_train_scaled, y_train)
        self.is_trained = True
        
        # Evaluate
        train_score = self.model.score(X_train_scaled, y_train)
        test_score = self.model.score(X_test_scaled, y_test)
        
        logger.info(f"Model trained - Train R²: {train_score:.4f}, Test R²: {test_score:.4f}")
        
        return {
            'train_score': train_score,
            'test_score': test_score,
            'n_samples': len(X)
        }
    
    def predict(self, features: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
        """
        Predict admission probability
        
        Args:
            features: Dictionary with student features
            
        Returns:
            Tuple of (probability, metadata)
        """
        if not self.is_trained:
            logger.warning("Model not trained, using mock prediction")
            return self._mock_prediction(features)
        
        # Prepare input
        X = pd.DataFrame([features])[self.feature_names]
        X['research_experience'] = int(X['research_experience'].iloc[0])
        
        # Scale and predict
        X_scaled = self.scaler.transform(X)
        probability = float(self.model.predict(X_scaled)[0])
        
        # Clip to [0, 1]
        probability = np.clip(probability, 0.0, 1.0)
        
        # Get feature importance (coefficients)
        feature_importance = self._get_feature_importance(X.values[0])
        
        metadata = {
            'model_type': 'Linear Regression',
            'confidence': self._calculate_confidence(probability),
            'feature_importance': feature_importance
        }
        
        return probability, metadata
    
    def _mock_prediction(self, features: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
        """Generate realistic mock prediction for demo purposes"""
        # Simple heuristic for demo
        gre_norm = (features['gre_score'] - 260) / 80  # Normalize 260-340 to 0-1
        toefl_norm = features['toefl_score'] / 120
        cgpa_norm = features['cgpa'] / 10
        research_boost = 0.1 if features['research_experience'] else 0
        
        probability = (
            0.3 * gre_norm +
            0.2 * toefl_norm +
            0.35 * cgpa_norm +
            0.1 * (features['university_rating'] / 5) +
            research_boost
        )
        probability = np.clip(probability, 0.0, 1.0)
        
        metadata = {
            'model_type': 'Mock Model (Demo)',
            'confidence': 'medium',
            'feature_importance': self._mock_feature_importance(features)
        }
        
        return probability, metadata
    
    def _get_feature_importance(self, feature_values: np.ndarray) -> Dict[str, float]:
        """Calculate feature importance using model coefficients"""
        coefficients = self.model.coef_
        importance = {}
        
        for i, name in enumerate(self.feature_names):
            # Contribution = coefficient * feature_value
            importance[name] = float(abs(coefficients[i] * feature_values[i]))
        
        # Normalize to sum to 1
        total = sum(importance.values())
        if total > 0:
            importance = {k: v/total for k, v in importance.items()}
        
        return importance
    
    def _mock_feature_importance(self, features: Dict[str, Any]) -> Dict[str, float]:
        """Generate mock feature importance"""
        return {
            'cgpa': 0.35,
            'gre_score': 0.25,
            'toefl_score': 0.15,
            'university_rating': 0.10,
            'lor_strength': 0.08,
            'sop_strength': 0.05,
            'research_experience': 0.02
        }
    
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
            'feature_names': self.feature_names
        }
        joblib.dump(model_data, path)
        logger.info(f"Model saved to {path}")
    
    def load_model(self, path: str):
        """Load trained model from disk"""
        model_data = joblib.load(path)
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.feature_names = model_data['feature_names']
        self.is_trained = True
        logger.info(f"Model loaded from {path}")

#!/usr/bin/env python3
"""
Test script for EduPredict AI API
Demonstrates the prediction endpoints
"""
import requests
import json

API_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("=" * 60)
    print("Testing Health Endpoint")
    print("=" * 60)
    response = requests.get(f"{API_URL}/api/v1/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print()

def test_admission_prediction():
    """Test admission prediction"""
    print("=" * 60)
    print("Testing Admission Prediction")
    print("=" * 60)
    
    payload = {
        "gre_score": 320,
        "toefl_score": 110,
        "university_rating": 4,
        "sop_strength": 4.5,
        "lor_strength": 4.0,
        "cgpa": 8.5,
        "research_experience": True
    }
    
    print("Request:")
    print(json.dumps(payload, indent=2))
    print()
    
    response = requests.post(
        f"{API_URL}/api/v1/predictions/admission",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    print("Response:")
    result = response.json()
    print(json.dumps(result, indent=2))
    print()
    
    # Print summary
    print("Summary:")
    print(f"  - Admission Probability: {result['admission_percentage']}%")
    print(f"  - Risk Level: {result['risk_level']}")
    print(f"  - Confidence: {result['confidence_level']}")
    print(f"  - Top Factor: {result['feature_importance'][0]['feature']} ({result['feature_importance'][0]['importance']})")
    print()

def test_dropout_prediction():
    """Test dropout prediction"""
    print("=" * 60)
    print("Testing Dropout Risk Prediction")
    print("=" * 60)
    
    payload = {
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
    
    print("Request:")
    print(json.dumps(payload, indent=2))
    print()
    
    response = requests.post(
        f"{API_URL}/api/v1/predictions/dropout",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    print("Response:")
    result = response.json()
    print(json.dumps(result, indent=2))
    print()
    
    # Print summary
    print("Summary:")
    print(f"  - Dropout Risk: {'YES' if result['dropout_risk'] else 'NO'}")
    print(f"  - Dropout Probability: {result['dropout_percentage']}%")
    print(f"  - Risk Level: {result['risk_level']}")
    print(f"  - Confidence: {result['confidence_level']}")
    print(f"  - Top Risk Factor: {result['feature_importance'][0]['feature']} ({result['feature_importance'][0]['importance']})")
    print(f"  - Recommendations: {len(result['recommendations'])} available")
    print()

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("EduPredict AI - API Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_health()
        test_admission_prediction()
        test_dropout_prediction()
        
        print("=" * 60)
        print("✅ All tests completed successfully!")
        print("=" * 60)
        print()
        print("📚 API Documentation: http://localhost:8000/docs")
        print()
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to API server")
        print("Please start the server first:")
        print("  cd backend && uvicorn app.main:app --reload")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()

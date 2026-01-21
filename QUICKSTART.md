# 🚀 Quick Start Guide

## Running the Backend

### Option 1: Direct Python

```bash
# Install dependencies
cd backend
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload

# Server will start at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Option 2: Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# API will be available at http://localhost:8000
```

## Testing the API

### Using curl

```bash
# Test health endpoint
curl http://localhost:8000/api/v1/health

# Test admission prediction
curl -X POST http://localhost:8000/api/v1/predictions/admission \
  -H "Content-Type: application/json" \
  -d '{
    "gre_score": 320,
    "toefl_score": 110,
    "university_rating": 4,
    "sop_strength": 4.5,
    "lor_strength": 4.0,
    "cgpa": 8.5,
    "research_experience": true
  }'

# Test dropout prediction
curl -X POST http://localhost:8000/api/v1/predictions/dropout \
  -H "Content-Type: application/json" \
  -d '{
    "age": 18,
    "gender": "male",
    "parent_education": "bachelors",
    "socio_economic_status": "medium",
    "attendance_rate": 85.5,
    "academic_grades": 75.0,
    "family_support": true,
    "distance_from_school": 5.0,
    "study_hours": 4.0
  }'
```

### Using Python Test Script

```bash
# Make sure server is running, then:
cd backend
python test_api.py
```

### Using Interactive API Docs

Open your browser and navigate to:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
.
├── backend/
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Configuration
│   │   ├── ml/           # Machine learning models
│   │   ├── schemas/      # Pydantic models
│   │   ├── services/     # Business logic
│   │   └── main.py       # FastAPI application
│   ├── tests/            # Unit tests
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Docker image
├── frontend/             # Next.js frontend (planned)
├── docker-compose.yml    # Multi-container setup
└── README.md            # This file
```

## Key Features Implemented

✅ **Backend API (FastAPI)**
- Admission probability prediction
- Dropout risk assessment
- Feature importance analysis
- Personalized recommendations
- Health check endpoints
- Comprehensive API documentation

✅ **ML Models**
- Linear Regression for admission prediction
- Random Forest for dropout classification
- Feature importance calculation
- Mock predictions for demo (training data needed)

✅ **DevOps**
- Docker containerization
- Docker Compose setup
- GitHub Actions CI/CD pipeline
- Environment configuration

✅ **Documentation**
- OpenAPI/Swagger docs
- Project specification
- Architecture diagrams
- Setup instructions

## Next Steps

1. **Train Real Models**: Replace mock predictions with trained models using real data
2. **Add Database**: Implement PostgreSQL for data persistence
3. **Add Caching**: Integrate Redis for prediction caching
4. **Build Frontend**: Create Next.js UI with Tailwind CSS
5. **Add Authentication**: Implement JWT-based user authentication
6. **Deploy**: Deploy to cloud platform (AWS/GCP)

## Development

```bash
# Run tests
cd backend
pytest

# Run linting
flake8 app
black --check app

# Format code
black app
```

## Support

For issues or questions:
- Open an issue on GitHub
- Email: ashwanip0009@gmail.com

## License

MIT License - See LICENSE file for details

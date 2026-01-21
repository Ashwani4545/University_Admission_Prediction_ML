# Contributing to EduPredict AI

Thank you for considering contributing to EduPredict AI! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### Reporting Issues
- Use the GitHub issue tracker
- Check if the issue already exists
- Provide detailed reproduction steps
- Include environment details (OS, Python version, etc.)

### Suggesting Features
- Open an issue with the "feature request" label
- Clearly describe the feature and its benefits
- Provide use cases and examples

### Submitting Pull Requests

1. **Fork the repository**
   ```bash
   git fork https://github.com/Ashwani4545/University_Admission_Prediction_ML.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style guide
   - Add tests for new functionality
   - Update documentation as needed

4. **Run tests**
   ```bash
   cd backend
   pytest
   flake8 app
   black --check app
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add: Brief description of changes"
   ```
   
   Commit message format:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for changes to existing features
   - `Docs:` for documentation changes
   - `Refactor:` for code refactoring

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Ensure all tests pass

## 📝 Code Style Guide

### Python (Backend)
- Follow PEP 8 style guide
- Use Black for code formatting
- Use flake8 for linting
- Type hints are encouraged
- Maximum line length: 100 characters
- Use docstrings for functions and classes

Example:
```python
def predict_admission(features: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
    """
    Predict university admission probability.
    
    Args:
        features: Dictionary containing student features
        
    Returns:
        Tuple of (probability, metadata)
    """
    # Implementation here
    pass
```

### TypeScript (Frontend - when implemented)
- Follow Airbnb style guide
- Use ESLint for linting
- Use Prettier for formatting
- Use TypeScript strict mode

## 🧪 Testing Guidelines

### Backend Tests
- Write unit tests for all new functions
- Use pytest fixtures for common setup
- Aim for >80% code coverage
- Test edge cases and error conditions

Example:
```python
def test_admission_prediction():
    """Test admission prediction endpoint"""
    features = {
        "gre_score": 320,
        "toefl_score": 110,
        "university_rating": 4,
        "sop_strength": 4.5,
        "lor_strength": 4.0,
        "cgpa": 8.5,
        "research_experience": True
    }
    result = predict_admission(features)
    assert 0 <= result[0] <= 1
```

## 📚 Documentation

- Update README.md for user-facing changes
- Update API documentation for endpoint changes
- Add docstrings for new functions/classes
- Update PROJECT_SPECIFICATION.md for architectural changes

## 🏗️ Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashwani4545/University_Admission_Prediction_ML.git
   cd University_Admission_Prediction_ML
   ```

2. **Set up Python environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the development server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Run tests**
   ```bash
   pytest
   ```

## 🔍 Code Review Process

All submissions require review. We use GitHub pull requests for this purpose.

### Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation is updated
- [ ] No breaking changes (or properly documented)
- [ ] Commit messages are clear
- [ ] Code is readable and maintainable

## 🐛 Bug Fix Process

1. Create an issue describing the bug
2. Reference the issue in your PR
3. Add tests that would have caught the bug
4. Ensure all existing tests still pass

## ✨ Feature Development Process

1. Discuss the feature in an issue first
2. Get approval from maintainers
3. Implement with tests
4. Update documentation
5. Submit PR for review

## 📋 Priority Areas for Contribution

### High Priority
- [ ] Frontend development (Next.js)
- [ ] Database integration (PostgreSQL)
- [ ] Authentication system (JWT)
- [ ] Model training with real data
- [ ] Comprehensive test suite

### Medium Priority
- [ ] Caching layer (Redis)
- [ ] Monitoring/observability
- [ ] Admin dashboard
- [ ] Mobile app
- [ ] Multi-language support

### Low Priority
- [ ] Additional ML models
- [ ] Advanced analytics
- [ ] Integration plugins
- [ ] Performance optimizations

## 🤔 Questions?

Feel free to:
- Open an issue for questions
- Email: ashwanip0009@gmail.com
- Start a discussion on GitHub

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to EduPredict AI! 🎓

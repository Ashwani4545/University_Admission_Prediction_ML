# 📘 Admission Prediction Using Machine Learning

## 🎯 Project Overview

This project predicts the probability of admission for students applying to universities based on their academic profiles.
The model uses the popular Admission_Predict.csv dataset and performs:

- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Visualization
- Model Selection using GridSearchCV
- Cross-validation
- Model Training (Linear Regression)
- Prediction for new student profiles


## 📁 Dataset Description

The dataset contains the following features:

| Feature           | Description                            |
| ----------------- | -------------------------------------- |
| GRE               | GRE exam score                         |
| TOEFL             | TOEFL exam score                       |
| University Rating | Rating of the applied university (1–5) |
| SOP               | Statement of Purpose strength          |
| LOR               | Letter of Recommendation strength      |
| CGPA              | Undergraduate CGPA                     |
| Research          | Research experience (0 or 1)           |
| Probability       | Probability of admission               |


## 🛠 Tech Stack

### Programming Language
- Python

### Libraries Used

- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- GridSearchCV
- Train-Test Split
- Linear Regression


## 📊 Exploratory Data Analysis (EDA)

### The project includes:
```
Histogram distribution of all major features
Checking missing values
Dataset structure & information
Statistical description
```
EDA helps understand feature patterns and data distribution before model building.

---

## 🧹 Data Cleaning

- Removed Serial No. column

- Replaced zeros in:
```
['GRE', 'TOEFL', 'University Rating', 'SOP', 'LOR', 'CGPA']
with NaN values
```

- Created a clean copy of the dataset for modeling

---

## 📦 Model Building
### ✔ Splitting Data
- Features (X): All independent variables
- Target (y): Probability of Admission
- Train-test split: 80% train, 20% test

### ✔ Model Selection with GridSearchCV
### Tested models:
- Linear Regression
- Lasso Regression
- Support Vector Regression
- Decision Tree Regressor
- Random Forest Regressor
- KNN Regressor

### ✔ Evaluation
Linear Regression performed the best with the highest accuracy.

---
## 🧪 Model Training
- Trained LinearRegression() model
- Achieved high test accuracy
- Final predictions made using the trained model

---
## 🧮 Example Predictions
```
model.predict([[337, 118, 4, 4.5, 4.5, 9.65, 0]])
model.predict([[320, 113, 2, 2.0, 2.5, 8.64, 1]])
```
Output is displayed in percentage probability of admission.

---
## 📈 Results
- Linear Regression achieved the best score among all algorithms
- The model accurately predicts admission probability
- Helps students estimate their chances based on academic metrics

---
## 📁 Project Structure
```
/data
    admission_predict.csv
/notebooks
    admission_prediction.ipynb
/src
    model.py (optional)
requirements.txt
README.md
LICENSE
```


## 🚀 How to Run the Project
1️⃣ Install required libraries:
```
pip install numpy pandas matplotlib scikit-learn
```
2️⃣ Run the notebook:
```
jupyter notebook admission_model.ipynb
```


## 🔮 Future Improvements

- Add feature scaling (StandardScaler)
- Add polynomial regression for better accuracy
- Deploy using Flask / Streamlit
- Build an interactive web UI
- Hyperparameter tuning with randomized search


## 📄License
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)


## 👤 Author

Ashwani Pandey

Machine Learning & Data Science Enthusiast

# 📘 Admission Prediction Using Machine Learning

## 🎯 Project Overview

This project predicts the probability of admission for students applying to universities based on their academic profiles.
The model uses the popular Admission_Predict.csv dataset and performs:

Exploratory Data Analysis (EDA)

Data Cleaning & Preprocessing

Visualization

Model Selection using GridSearchCV

Cross-validation

Model Training (Linear Regression)

Prediction for new student profiles

---

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

---

## 🛠 Tech Stack

### Programming Language
Python

### Libraries Used

- NumPy

- Pandas

- Matplotlib

- Scikit-learn

- GridSearchCV

- Train-Test Split

- Linear Regression

---

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

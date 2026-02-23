# 📘 University Admission Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellowgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## 🎯 Project Overview

This project predicts the **probability of admission** for students applying to universities based on their academic profiles.
It uses the `admission_predict.csv` dataset and covers the full ML pipeline:

- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Data Visualization
- Model Selection using GridSearchCV
- Model Training (Linear Regression)
- Prediction for new student profiles

---

## 📁 Dataset Description

**File:** `admission_predict.csv` (500 records)

The dataset contains the following features:

| Column            | Description                              |
| ----------------- | ---------------------------------------- |
| Serial No.        | Unique row identifier (dropped in model) |
| GRE Score         | GRE exam score (out of 340)              |
| TOEFL Score       | TOEFL exam score (out of 120)            |
| University Rating | Rating of the university applied to (1–5)|
| SOP               | Strength of Statement of Purpose (1–5)   |
| LOR               | Strength of Letter of Recommendation (1–5)|
| CGPA              | Undergraduate CGPA (out of 10)           |
| Research          | Research experience — 0 (No) / 1 (Yes)  |
| Chance of Admit   | Probability of admission (0–1)           |

---

## 🛠 Tech Stack

| Category          | Tools / Libraries                        |
| ----------------- | ---------------------------------------- |
| Language          | Python 3                                 |
| Data Handling     | NumPy, Pandas                            |
| Visualization     | Matplotlib                               |
| Machine Learning  | scikit-learn (LinearRegression, Lasso, SVR, DecisionTree, RandomForest, KNN, GridSearchCV) |
| Notebook          | Jupyter Notebook                         |

---

## 📊 Exploratory Data Analysis (EDA)

The project includes:

- Shape, data types, and statistical summary of the dataset
- Null value detection
- Histogram distributions for all major features:
  - GRE Score, TOEFL Score, University Rating, SOP, LOR, CGPA, Research

---

## 🧹 Data Cleaning

- Renamed columns for convenience:
  - `GRE Score` → `GRE`, `TOEFL Score` → `TOEFL`, `LOR ` → `LOR`, `Chance of Admit ` → `Probability`
- Dropped the `Serial No.` column (not a predictive feature)
- Replaced zero values in `['GRE', 'TOEFL', 'University Rating', 'SOP', 'LOR', 'CGPA']` with `NaN`
- Created a deep copy of the cleaned dataset for modeling

---

## 📦 Model Building

### ✔ Splitting Data
- **Features (X):** All columns except `Chance of Admit`
- **Target (y):** `Chance of Admit` (renamed to `Probability`)
- **Split:** 80% train / 20% test

### ✔ Model Selection with GridSearchCV

The following models were evaluated:

| Model                   | Hyperparameters Tuned                        |
| ----------------------- | -------------------------------------------- |
| Linear Regression       | `normalize`                                  |
| Lasso Regression        | `alpha`, `selection`                         |
| Support Vector Regressor| `gamma`                                      |
| Decision Tree Regressor | `criterion`, `splitter`                      |
| Random Forest Regressor | `n_estimators`                               |
| KNN Regressor           | `n_neighbors`                                |

### ✔ Result
**Linear Regression** achieved the best cross-validated score and was selected as the final model.

---

## 🧪 Model Training & Evaluation

- Final model: `LinearRegression()`
- Fitted on 80% of the dataset
- Evaluated on the held-out 20% test set

---

## 🧮 Example Predictions

```python
# High-achieving student profile
model.predict([[337, 118, 4, 4.5, 4.5, 9.65, 0]])

# Average student profile
model.predict([[320, 113, 2, 2.0, 2.5, 8.64, 1]])
```

Output is the predicted probability of admission (e.g., `0.89` = 89% chance).

---

## 📈 Results

- Linear Regression outperformed all other tested algorithms
- The model accurately estimates admission probability based on academic metrics
- Can help students gauge their chances before applying

---

## 📁 Project Structure

```
University_Admission_Prediction_ML/
├── admission_predict.csv       # Dataset
├── Admission prediction.ipynb  # Main Jupyter Notebook
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

---

## 🚀 How to Run the Project

**1. Clone the repository**
```bash
git clone https://github.com/Ashwani4545/University_Admission_Prediction_ML.git
cd University_Admission_Prediction_ML
```

**2. Install required libraries**
```bash
pip install -r requirements.txt
```

**3. Launch the Jupyter Notebook**
```bash
jupyter notebook "Admission prediction.ipynb"
```

---

## 🔮 Future Improvements

- Add feature scaling with `StandardScaler`
- Explore polynomial regression for non-linear relationships
- Deploy using Flask or Streamlit as an interactive web app
- Hyperparameter tuning with `RandomizedSearchCV`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Ashwani Pandey**  
Machine Learning & Data Science Enthusiast

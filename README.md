# Customer Churn Analysis and Prediction

This repository contains a Jupyter Notebook (`Churn.ipynb`) that experiments with several machine learning algorithms to predict customer churn using the Telco Customer Churn dataset.

## Problem Statement

Customer churn directly impacts revenue and business growth. This project helps identify which customers are likely to leave, enabling:
- Proactive retention strategies for high-value customers
- Improved customer lifetime value through targeted interventions
- Data-driven insights into factors influencing customer loyalty


## Overview
- Goal: Compare multiple models (Logistic Regression, KNN, SVC, Naive Bayes, Decision Tree, Random Forest) to identify which generalizes best for churn prediction.
- Notebook: `Churn.ipynb` (run in Jupyter or VS Code).
- Data: `data/Telco Customer Churn Dataset.csv`.
``

## Models Evaluated
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Naive Bayes (GaussianNB)
- Decision Tree (criterion='entropy', max_depth=5)
- Random Forest (n_estimators=100, max_depth=5)
``

## Reported Model Accuracies (from notebook summary)

| Model                | Training Accuracy | Testing Accuracy |
|---------------------:|------------------:|-----------------:|
| Random Forest        | 0.8389            | 0.7978           |
| Logistic Regression  | 0.8176            | 0.7989           |
| Decision Tree        | 0.8233            | 0.7678           |
| KNN                  | 0.8048            | 0.7703           |
| SVC                  | 0.8226            | 0.7893           |
| Naive Bayes          | 0.7686            | 0.7549           |
``

## Evaluation Metrics
The notebook prints for each model:
- Accuracy
- Classification report (precision, recall, f1-score)
- Confusion matrix

## How to run
1. Create and activate a Python environment (recommended Python 3.8+).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open `Churn.ipynb` in Jupyter or VS Code and run all cells.

## Findings & Next Steps
- Logistic Regression and Random Forest are the most promising models: Logistic Regression shows good generalization, Random Forest achieves highest accuracy but with some overfitting.
- Suggested improvements:
  - Hyperparameter tuning (GridSearchCV / RandomizedSearchCV).
  - Cross-validation for more robust performance estimates.
  - Feature engineering and selection to improve generalization.
  - Try ensemble boosting methods (e.g., XGBoost, LightGBM).

## Files
- `Churn.ipynb` — analysis and model training.
- `data/Telco Customer Churn Dataset.csv` — dataset used.
- `requirements.txt` — Python dependencies.

---
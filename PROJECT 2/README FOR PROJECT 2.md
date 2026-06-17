# 🌸 Iris Flower Classification — K-Nearest Neighbors (KNN)
**Project 2 | Artificial Intelligence Track**
**Batch: 2026 | Powered by DecodeLabs**

---

## 📌 Project Overview

This project builds a supervised machine learning model that classifies iris flowers into one of three species — **Setosa**, **Versicolor**, or **Virginica** — based on four physical measurements. Unlike Project 1's rule-based logic, this model **learns patterns from data** rather than following hardcoded if-else rules.

This marks the shift from deterministic logic to **Supervised Learning**, the predictive phase of the AI Engineering track at DecodeLabs.

---

## 🎯 Goal

Build a basic classification model using the Iris dataset that can predict a flower's species from its measurements.

---

## ⚙️ How It Works (IPO Framework)

| Stage | What Happens |
|---|---|
| **Input** | Iris dataset (150 samples, 4 features, 3 classes) is loaded and features are scaled |
| **Process** | Data is split into training/testing sets, and a K-Nearest Neighbors model is trained |
| **Output** | Model predictions are evaluated using a Confusion Matrix and F1 Score |

---

## 🧠 Key Concepts Used

- **Dataset Loading** — Iris dataset loaded directly from `sklearn.datasets`
- **Feature Scaling** — `StandardScaler` normalizes all 4 features to mean=0, variance=1, since KNN is distance-based
- **Train-Test Split** — 80% training, 20% testing (`stratify=y` keeps class balance equal in both sets)
- **K Selection (Elbow Method)** — Tests K values from 1–20 and picks the one with the lowest error rate
- **KNN Algorithm** — Classifies new data points based on the majority vote of their nearest neighbors
- **Scikit-Learn Workflow** — Instantiate → Fit → Predict
- **Model Evaluation** — Accuracy, F1 Score, Confusion Matrix, and full Classification Report
- **Sample Prediction** — Tests the trained model on a brand-new, unseen flower measurement

---

## 🗂️ Project Structure

```
Project2-IrisKNN/
│
├── iris_knn_classifier.py   # Main script
├── elbow_curve.png          # K-value optimization chart
├── confusion_matrix.png     # Model evaluation chart
└── README.md                 # Project documentation
```

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Install the required libraries:

```bash
pip install scikit-learn matplotlib numpy
```

3. Run the script:

```bash
python iris_knn_classifier.py
```

4. The script will print results to the console and save two chart images (`elbow_curve.png` and `confusion_matrix.png`) in the same folder.

---

## 📊 Results Summary

| Metric | Value |
|---|---|
| Optimal K | 1 |
| Accuracy | 96.67% |
| F1 Score (weighted) | 0.97 |
| Training samples | 120 |
| Testing samples | 30 |

**Confusion Matrix:**

```
              Predicted
              Setosa  Versicolor  Virginica
Actual Setosa     10       0          0
   Versicolor      0      10          0
    Virginica      0       1          9
```

Only **1 misclassification** out of 30 test samples — a Virginica flower predicted as Versicolor.

---

## 🌼 Sample Prediction

```
Input measurements: [5.1, 3.5, 1.4, 0.2]
Predicted species: setosa
```

---

## 📋 Specification Checklist

- [x] Load and understand a dataset — Iris dataset loaded with full feature/class breakdown
- [x] Split data into training and testing sets — 80/20 stratified split
- [x] Apply a simple classification algorithm — K-Nearest Neighbors
- [x] Feature scaling applied (StandardScaler)
- [x] Optimal K determined using the Elbow Method
- [x] Model evaluated with Confusion Matrix and F1 Score

---

## 🔑 Key Skills Demonstrated

- Data handling and exploration with Scikit-Learn
- Supervised learning fundamentals
- Feature scaling and its importance in distance-based algorithms
- Model training, prediction, and evaluation
- Interpreting confusion matrices and classification metrics
- Hyperparameter tuning (choosing optimal K)

---

## 👨‍💻 Author

**Marvin Tettey | DecodeLabs AI Intern — Batch 2026**

---

*"We do not write the rules. We provide history, and the machine derives the logic."*
*— DecodeLabs*

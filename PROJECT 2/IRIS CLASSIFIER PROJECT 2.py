# Decode Labs - Artificial Intelligence Project 2
# Data Classification Using AI (K-Nearest Neighbors)
# Dataset: Iris Flower Dataset
# Developed by: Marvin Tettey

# ---------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    f1_score
)

print("=" * 60)
print("🌸 DecodeLabs AI Project 2: Iris Flower Classification 🌸")
print("Algorithm: K-Nearest Neighbors (KNN)")
print("=" * 60)

# ---------------------------------------------------
# STEP 2: LOAD AND UNDERSTAND THE DATASET
# ---------------------------------------------------
# The Iris dataset has 150 samples, 4 features, and 3 classes
# Features: sepal length, sepal width, petal length, petal width
# Classes: Setosa, Versicolor, Virginica

iris = load_iris()
X = iris.data            # Features (measurements)
y = iris.target          # Labels (flower species)
feature_names = iris.feature_names
target_names = iris.target_names

print("\n📊 DATASET OVERVIEW")
print(f"Total samples: {X.shape[0]}")
print(f"Total features: {X.shape[1]}")
print(f"Feature names: {feature_names}")
print(f"Classes: {list(target_names)}")
print(f"Samples per class: {np.bincount(y)}")

# ---------------------------------------------------
# STEP 3: SPLIT THE DATA (TRAIN / TEST)
# ---------------------------------------------------
# 80% training, 20% testing — random_state ensures repeatable results
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y  # keeps class proportions balanced in both sets
)

print("\n✂️  DATA SPLIT")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# ---------------------------------------------------
# STEP 4: SCALE THE FEATURES
# ---------------------------------------------------
# KNN relies on distance calculations, so all features must be
# on the same scale. StandardScaler transforms data to have
# mean = 0 and variance = 1.

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n⚖️  FEATURE SCALING")
print("Features scaled using StandardScaler (mean=0, variance=1)")

# ---------------------------------------------------
# STEP 5: FIND THE OPTIMAL VALUE OF K (ELBOW METHOD)
# ---------------------------------------------------
print("\n🔍 FINDING OPTIMAL K VALUE...")

error_rates = []
k_range = range(1, 21)

for k in k_range:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, y_train)
    pred_temp = knn_temp.predict(X_test_scaled)
    error_rates.append(np.mean(pred_temp != y_test))

best_k = k_range[np.argmin(error_rates)]
print(f"Optimal K found: {best_k} (lowest error rate: {min(error_rates):.4f})")

# Plot the elbow curve and save it as an image
plt.figure(figsize=(8, 5))
plt.plot(k_range, error_rates, marker='o', linestyle='--', color='blue')
plt.axvline(x=best_k, color='red', linestyle=':', label=f'Optimal K = {best_k}')
plt.title('Elbow Method: Choosing the Best K')
plt.xlabel('K Value')
plt.ylabel('Error Rate')
plt.legend()
plt.grid(True)
plt.savefig('elbow_curve.png', dpi=150, bbox_inches='tight')
print("📈 Elbow curve saved as 'elbow_curve.png'")
plt.close()

# ---------------------------------------------------
# STEP 6: TRAIN THE FINAL KNN MODEL
# ---------------------------------------------------
# Following the Scikit-Learn workflow: Instantiate -> Fit -> Predict

model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train_scaled, y_train)

print(f"\n🤖 MODEL TRAINED")
print(f"Algorithm: K-Nearest Neighbors with K={best_k}")

# ---------------------------------------------------
# STEP 7: MAKE PREDICTIONS
# ---------------------------------------------------
predictions = model.predict(X_test_scaled)

# ---------------------------------------------------
# STEP 8: EVALUATE THE MODEL
# ---------------------------------------------------
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')
cm = confusion_matrix(y_test, predictions)

print("\n" + "=" * 60)
print("📋 MODEL EVALUATION RESULTS")
print("=" * 60)
print(f"Accuracy:  {accuracy * 100:.2f}%")
print(f"F1 Score:  {f1:.4f}")

print("\n🧮 CONFUSION MATRIX")
print(cm)

print("\n📑 CLASSIFICATION REPORT")
print(classification_report(y_test, predictions, target_names=target_names))

# Plot and save the confusion matrix as an image
plt.figure(figsize=(6, 5))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(len(target_names))
plt.xticks(tick_marks, target_names, rotation=45)
plt.yticks(tick_marks, target_names)

# Add the numbers inside the matrix boxes
thresh = cm.max() / 2.0
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, format(cm[i, j], 'd'),
                 ha="center", va="center",
                 color="white" if cm[i, j] > thresh else "black")

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150, bbox_inches='tight')
print("\n📈 Confusion matrix chart saved as 'confusion_matrix.png'")
plt.close()

# ---------------------------------------------------
# STEP 9: TEST WITH A SAMPLE PREDICTION
# ---------------------------------------------------
print("\n" + "=" * 60)
print("🌼 SAMPLE PREDICTION TEST")
print("=" * 60)

sample_flower = [[5.1, 3.5, 1.4, 0.2]]  # Example measurements
sample_scaled = scaler.transform(sample_flower)
sample_prediction = model.predict(sample_scaled)

print(f"Input measurements: {sample_flower[0]}")
print(f"Predicted species: {target_names[sample_prediction[0]]}")

print("\n✅ Project 2 completed successfully!")

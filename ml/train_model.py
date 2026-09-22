import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load manufacturing dataset
data = pd.read_csv("../data/manufacturing_data.csv")

# Features used by FactoryDNA
features = [
    "temperature",
    "pressure",
    "speed",
    "vibration",
    "energy_consumption",
    "raw_material_usage",
    "production_quality"
]

X = data[features]
y = data["waste"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create the ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train FactoryDNA
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("FACTORYDNA AI - MODEL TRAINING")
print("=" * 50)

print(f"\nTraining records: {len(X_train)}")
print(f"Testing records:  {len(X_test)}")
print(f"Model Accuracy:   {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Show importance of each manufacturing parameter
print("\nFeature Importance:")
for feature, importance in zip(features, model.feature_importances_):
    print(f"{feature:25s}: {importance:.4f}")

# Save trained model
joblib.dump(model, "factorydna_model.pkl")

print("\nModel saved successfully!")
print("File: factorydna_model.pkl")
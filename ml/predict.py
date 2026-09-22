import pandas as pd
import joblib

# Load trained FactoryDNA model
model = joblib.load("factorydna_model.pkl")

features = [
    "temperature",
    "pressure",
    "speed",
    "vibration",
    "energy_consumption",
    "raw_material_usage",
    "production_quality"
]

print("=" * 60)
print("             FACTORYDNA AI")
print("       Manufacturing Waste Predictor")
print("=" * 60)

# Example current machine conditions
machine_data = {
    "temperature": 88,
    "pressure": 8.2,
    "speed": 1650,
    "vibration": 5.0,
    "energy_consumption": 88,
    "raw_material_usage": 110,
    "production_quality": 82
}

input_data = pd.DataFrame([machine_data])

# Prediction
prediction = model.predict(input_data[features])[0]

# Probability
probability = model.predict_proba(input_data[features])[0][1] * 100

print("\nCURRENT MACHINE CONDITIONS")
print("-" * 60)

for parameter, value in machine_data.items():
    print(f"{parameter:25s}: {value}")

print("\nFACTORYDNA PREDICTION")
print("-" * 60)

if probability >= 70:
    risk = "HIGH"
    symbol = "[HIGH RISK]"
elif probability >= 40:
    risk = "MEDIUM"
    symbol = "[MEDIUM RISK]"
else:
    risk = "LOW"
    symbol = "[LOW RISK]"

print(f"Waste Probability : {probability:.2f}%")
print(f"Risk Level        : {symbol}")

if prediction == 1:
    print("\nWARNING: Potential waste/defect condition detected.")
else:
    print("\nMachine condition appears normal.")

print("\nRECOMMENDATION")
print("-" * 60)

if risk == "HIGH":
    print("1. Reduce machine speed.")
    print("2. Check temperature and bring it toward the optimal range.")
    print("3. Inspect vibration levels.")
    print("4. Monitor energy consumption.")

elif risk == "MEDIUM":
    print("1. Monitor temperature and machine speed.")
    print("2. Check vibration levels.")
    print("3. Continue monitoring production quality.")

else:
    print("1. Continue current operating conditions.")
    print("2. Continue monitoring machine parameters.")

print("\n" + "=" * 60)

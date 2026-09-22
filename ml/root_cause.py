import pandas as pd
import joblib

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

probability = model.predict_proba(input_data[features])[0][1] * 100

importances = model.feature_importances_

importance_df = pd.DataFrame({
    "parameter": features,
    "importance": importances,
    "value": [machine_data[x] for x in features]
})

importance_df["contribution"] = (
    importance_df["importance"] /
    importance_df["importance"].sum()
) * 100

importance_df = importance_df.sort_values(
    by="contribution",
    ascending=False
)

print("=" * 60)
print("              FACTORYDNA AI")
print("             ROOT CAUSE ANALYSIS")
print("=" * 60)

print(f"\nWaste Probability: {probability:.2f}%")

print("\nTOP CONTRIBUTING PARAMETERS")
print("-" * 60)

for _, row in importance_df.head(5).iterrows():
    print(
        f"{row['parameter']:25s} "
        f"{row['contribution']:.2f}%"
    )

print("\nINTERPRETATION")
print("-" * 60)

for _, row in importance_df.head(3).iterrows():

    parameter = row["parameter"]

    if parameter == "temperature":
        print("→ Temperature has significant influence on the prediction.")

    elif parameter == "speed":
        print("→ Machine speed is a major contributing factor.")

    elif parameter == "vibration":
        print("→ High vibration may indicate unstable machine operation.")

    elif parameter == "energy_consumption":
        print("→ High energy consumption may indicate inefficient operation.")

    elif parameter == "pressure":
        print("→ Pressure variation may affect production conditions.")

    elif parameter == "raw_material_usage":
        print("→ Raw material usage contributes to the process condition.")

    elif parameter == "production_quality":
        print("→ Production quality strongly influences the predicted outcome.")

print("\nRECOMMENDED ACTIONS")
print("-" * 60)

if machine_data["speed"] > 1500:
    print("→ Reduce machine speed toward the learned operating range.")

if machine_data["temperature"] > 85:
    print("→ Reduce or stabilize operating temperature.")

if machine_data["vibration"] > 4:
    print("→ Inspect the machine for abnormal vibration.")

if machine_data["energy_consumption"] > 80:
    print("→ Monitor energy consumption for inefficient operation.")

print("\n" + "=" * 60)
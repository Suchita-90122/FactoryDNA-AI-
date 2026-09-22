from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

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


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "FactoryDNA AI Prediction Service",
        "status": "running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data[features])[0]

    probability = model.predict_proba(
        input_data[features]
    )[0][1] * 100

    if probability >= 70:
        risk = "HIGH"
    elif probability >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    if prediction == 1:
        result = "WASTE"
    else:
        result = "NORMAL"

    return jsonify({
        "prediction": result,
        "waste_probability": round(probability, 2),
        "risk_level": risk
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
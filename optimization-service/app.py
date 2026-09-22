from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "service": "FactoryDNA Root Cause and Optimization Service",
        "status": "running"
    })


@app.route("/api/optimize", methods=["POST"])
def optimize():

    data = request.get_json()

    recommendations = []
    contributors = []

    if data["production_quality"] < 80:
        contributors.append({
            "parameter": "production_quality",
            "reason": "Low production quality may increase waste risk",
            "impact": "HIGH"
        })

        recommendations.append(
            "Improve production quality and maintain stable operating conditions"
        )

    if data["speed"] > 1600:
        contributors.append({
            "parameter": "speed",
            "reason": "High machine speed may increase waste",
            "impact": "HIGH"
        })

        recommendations.append(
            "Reduce machine speed to a stable operating range"
        )

    if data["temperature"] > 90:
        contributors.append({
            "parameter": "temperature",
            "reason": "High temperature may affect production stability",
            "impact": "MEDIUM"
        })

        recommendations.append(
            "Reduce and stabilize machine temperature"
        )

    if data["vibration"] > 5:
        contributors.append({
            "parameter": "vibration",
            "reason": "High vibration may indicate machine instability",
            "impact": "MEDIUM"
        })

        recommendations.append(
            "Inspect the machine for excessive vibration"
        )

    if data["energy_consumption"] > 90:
        contributors.append({
            "parameter": "energy_consumption",
            "reason": "High energy consumption may indicate inefficient operation",
            "impact": "MEDIUM"
        })

        recommendations.append(
            "Monitor energy consumption and improve machine efficiency"
        )

    if data["raw_material_usage"] > 110:
        contributors.append({
            "parameter": "raw_material_usage",
            "reason": "High material usage may contribute to production waste",
            "impact": "MEDIUM"
        })

        recommendations.append(
            "Optimize raw material usage"
        )

    return jsonify({
        "status": "analysis completed",
        "root_cause_contributors": contributors,
        "optimization_recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(port=5004, debug=True)
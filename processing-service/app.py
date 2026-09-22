from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "service": "FactoryDNA Data Processing Service",
        "status": "running"
    })

@app.route("/api/process", methods=["POST"])
def process_data():
    data = request.get_json()

    processed_data = {
        "temperature": float(data["temperature"]),
        "pressure": float(data["pressure"]),
        "speed": float(data["speed"]),
        "vibration": float(data["vibration"]),
        "energy_consumption": float(data["energy_consumption"]),
        "raw_material_usage": float(data["raw_material_usage"]),
        "production_quality": float(data["production_quality"])
    }

    return jsonify({
        "message": "Data processed successfully",
        "processed_data": processed_data
    })

if __name__ == "__main__":
    app.run(port=5002, debug=True)
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow the frontend running on port 8000
CORS(app)

# FactoryDNA microservices
IOT_URL = "http://127.0.0.1:5001/api/sensor"
PROCESSING_URL = "http://127.0.0.1:5002/api/process"
AI_URL = "http://127.0.0.1:5000/predict"
OPTIMIZATION_URL = "http://127.0.0.1:5004/api/optimize"


@app.route("/")
def home():
    return jsonify({
        "service": "FactoryDNA Integration Service",
        "status": "running"
    })


@app.route("/api/pipeline", methods=["GET"])
def pipeline():

    # -----------------------------------
    # 1. Get live IoT sensor data
    # -----------------------------------
    sensor_response = requests.get(IOT_URL)
    sensor_response.raise_for_status()

    sensor_data = sensor_response.json()


    # -----------------------------------
    # 2. Process the sensor data
    # -----------------------------------
    processing_response = requests.post(
        PROCESSING_URL,
        json=sensor_data
    )

    processing_response.raise_for_status()

    processing_result = processing_response.json()

    processed_data = processing_result["processed_data"]


    # -----------------------------------
    # 3. AI waste prediction
    # -----------------------------------
    ai_response = requests.post(
        AI_URL,
        json=processed_data
    )

    ai_response.raise_for_status()

    ai_result = ai_response.json()


    # -----------------------------------
    # 4. Root cause + optimization
    # -----------------------------------
    optimization_response = requests.post(
        OPTIMIZATION_URL,
        json=processed_data
    )

    optimization_response.raise_for_status()

    optimization_result = optimization_response.json()


    # -----------------------------------
    # 5. Return complete FactoryDNA result
    # -----------------------------------
    return jsonify({

        "iot_data": sensor_data,

        "processing_result": processing_result,

        "ai_prediction": ai_result,

        "optimization": optimization_result

    })


# -----------------------------------
# Start Integration Service
# -----------------------------------
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5003,
        debug=True
    )
from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)


def generate_sensor_data():

    data = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),

        "temperature": round(random.uniform(70, 100), 2),

        "pressure": round(random.uniform(6, 10), 2),

        "speed": round(random.uniform(1200, 1900), 2),

        "vibration": round(random.uniform(2, 7), 2),

        "energy_consumption": round(random.uniform(60, 110), 2),

        "raw_material_usage": round(random.uniform(80, 125), 2),

        "production_quality": round(random.uniform(60, 98), 2)
    }

    return data


@app.route("/")
def home():
    return jsonify({
        "service": "FactoryDNA IoT Data Collection Service",
        "status": "running"
    })


@app.route("/api/sensor")
def sensor():

    data = generate_sensor_data()

    return jsonify(data)


@app.route("/api/sensors")
def sensors():

    readings = []

    for i in range(10):
        readings.append(generate_sensor_data())

    return jsonify(readings)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
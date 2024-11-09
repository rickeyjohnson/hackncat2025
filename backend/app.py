# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app, resources={r"/metrics": {"origins": "http://127.0.0.1:5500"}})

def get_random_energy_metrics():
    # Simulating energy consumption with random numbers
    cpu_usage = random.uniform(10, 100)           # Random CPU usage between 10% and 100%
    ram_usage = random.uniform(10, 100)            # Random RAM usage between 10% and 100%
    disk_usage = random.uniform(10, 100)           # Random Disk usage between 10% and 100%

    # Simulated total energy consumption
    total_consumption = cpu_usage + ram_usage + disk_usage
    
    metrics = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
        "total_consumption": total_consumption
    }
    return metrics

@app.route('/metrics')
def metrics():
    return jsonify(get_random_energy_metrics())

if __name__ == '__main__':
    app.run(debug=True)

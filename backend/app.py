# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import time

app = Flask(__name__)
CORS(app)

def get_energy_metrics():
    # Simulating energy usage with basic system metrics
    cpu_usage = psutil.cpu_percent(interval=1)            # CPU usage in %
    ram_usage = psutil.virtual_memory().percent            # RAM usage in %
    disk_usage = psutil.disk_usage('/').percent            # Disk usage in %
    # You could add additional measurements or calculations if you have a way to measure energy directly

    metrics = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
        "total_consumption": cpu_usage + ram_usage + disk_usage  # Simulated total energy consumption
    }
    return metrics

@app.route('/metrics')
def metrics():
    return jsonify(get_energy_metrics())

if __name__ == '__main__':
    app.run(debug=True)
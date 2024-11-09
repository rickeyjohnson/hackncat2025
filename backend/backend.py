# backend.py
from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)

@app.route('/metrics')
def get_metrics():
    # Gather metrics
    cpu_usage = psutil.cpu_percent(interval=0.5)  # CPU usage in percentage
    ram_usage = psutil.virtual_memory().percent   # RAM usage in percentage
    storage_usage = psutil.disk_usage('/').percent  # Disk usage in percentage
    # You could add logic here for total power consumption if you have the data
    
    metrics = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "storage_usage": storage_usage,
        "total_consumption": cpu_usage + ram_usage + storage_usage  # Placeholder example
    }
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, jsonify
# from flask_cors import CORS
# import psutil
# import time

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# @app.route('/metrics')
# def get_metrics():
#     cpu_usage = psutil.cpu_percent(interval=0.5)
#     ram_usage = psutil.virtual_memory().percent
#     storage_usage = psutil.disk_usage('/').percent
#     metrics = {
#         "time": time.strftime("%Y-%m-%d %H:%M:%S"),
#         "cpu_usage": cpu_usage,
#         "ram_usage": ram_usage,
#         "storage_usage": storage_usage,
#         "total_consumption": cpu_usage + ram_usage + storage_usage
#     }
#     return jsonify(metrics)

# if __name__ == '__main__':
#     app.run(debug=True)

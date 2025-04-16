import random
import time
import json
import requests
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import threading

# Initialize Flask app
app = Flask(__name__)

# Function to simulate IoT data (CNC machine)
def generate_iot_data():
    data = {
        "coordinates": (random.uniform(0, 100), random.uniform(0, 100)),
        "spindle_speed": random.randint(1000, 5000),  # Spindle speed in RPM
        "feed_rate": random.randint(10, 1000),  # Feed rate in mm/min
        "tool_number": random.randint(1, 10),
    }
    return data

# Data Preprocessing (Normalization)
def preprocess_data(data):
    features = []
    for point in data:
        features.append([point['coordinates'][0], point['coordinates'][1], point['spindle_speed'], point['feed_rate']])
    scaler = StandardScaler()
    return scaler.fit_transform(features)

# Anomaly Detection using Isolation Forest
def detect_anomalies(X_train):
    model = IsolationForest(contamination=0.1)
    model.fit(X_train)
    return model

# API endpoint to receive IoT data
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()  # Get data sent by the IoT device
    print(f"Received data: {data}")
    
    # Preprocess and detect anomaly
    X_train = preprocess_data([data])  # Process the incoming data
    model = detect_anomalies(X_train)  # Train the model
    prediction = model.predict(X_train)
    
    # If anomaly is detected (prediction == -1)
    if prediction[0] == -1:
        print(f"Anomaly Detected: {data}")
    else:
        print(f"Normal Data: {data}")
    
    return jsonify({"message": "Data received successfully"}), 200

# Simulate sending data to the Flask server (IoT Client)
def send_data_to_server():
    url = "http://localhost:5000/api/data"  # Server endpoint

    # Retry until the Flask server is ready
    while True:
        try:
            data = generate_iot_data()
            response = requests.post(url, json=data)  # Send data to the server
            if response.status_code == 200:
                print(f"Data sent successfully: {data}")
            else:
                print(f"Failed to send data: {response.status_code}")
            time.sleep(5)  # Send data every 5 seconds
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error: {e}. Retrying...")
            time.sleep(1)  # Wait for 1 second before retrying

# Run the Flask server in the main thread
def run_server():
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Start the Flask server in the main thread (this blocks further execution until server is stopped)
    print("Starting Flask server...")
    run_server()  # Running the server in the main thread directly

    # Wait for the server to start and be ready
    print("Waiting for server to start...")

    # Ensure the server has time to initialize before starting the IoT simulation
    server_ready = False
    while not server_ready:
        try:
            response = requests.get("http://localhost:5000")
            if response.status_code == 200:
                server_ready = True
                print("Flask server is ready!")
            else:
                print("Server not ready yet...")
                time.sleep(1)  # Wait 1 second before retrying
        except requests.exceptions.ConnectionError:
            print("Server not available yet. Retrying...")
            time.sleep(1)  # Retry every 1 second

    # Once Flask server is ready, start sending IoT data to the server
    print("Starting IoT simulation...")
    send_data_to_server()


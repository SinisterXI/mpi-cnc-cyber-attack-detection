from sklearn.metrics import classification_report

# Example data: This should be replaced by actual data from simulator.py or parse_gcode.py
data_points = [
    {'coordinates': (10, 20, 30), 'spindle_speed': 3000, 'feed_rate': 500, 'coolant_status': 'ON', 'true_label': 0},
    {'coordinates': (150, 160, 170), 'spindle_speed': 6000, 'feed_rate': 20, 'coolant_status': 'ON', 'true_label': 1},  # Anomaly: Spindle speed and coordinates
    {'coordinates': (30, 40, 50), 'spindle_speed': 2500, 'feed_rate': 400, 'coolant_status': 'ON', 'true_label': 0},
    {'coordinates': (70, 80, 90), 'spindle_speed': 4000, 'feed_rate': 600, 'coolant_status': 'OFF', 'true_label': 1},  # Anomaly: Coolant off
    {'coordinates': (90, 100, 110), 'spindle_speed': 5200, 'feed_rate': 50, 'coolant_status': 'OFF', 'true_label': 1}  # Anomaly: Spindle speed and coolant
]

# Updated anomaly detection system
def detect_anomaly(data_point):
    # Define anomaly detection rules based on updated simulator/parse logic
    if (data_point['spindle_speed'] > 5000 or  # Spindle speed anomaly
        data_point['feed_rate'] < 10 or  # Feed rate anomaly
        data_point['coordinates'][0] > 100 or data_point['coordinates'][1] > 100 or data_point['coordinates'][2] > 100 or  # Tool path anomaly
        data_point['coolant_status'] == 'OFF'):  # Coolant anomaly
        return 1  # Anomaly
    else:
        return 0  # Normal

# Step 3: Collect true labels and predicted labels
true_labels = []  # Ground truth (actual labels)
predicted_labels = []  # Predicted labels by the anomaly detection system

# Apply the anomaly detection system on the data
for data_point in data_points:
    true_labels.append(data_point['true_label'])
    predicted_labels.append(detect_anomaly(data_point))

# Step 4: Calculate the classification report
print("Classification Report:")
print(classification_report(true_labels, predicted_labels))


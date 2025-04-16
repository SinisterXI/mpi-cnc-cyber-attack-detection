import random

def simulate_runtime_data():
    return {
        'coordinates': (random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)),
        'spindle_speed': random.randint(100, 5000),
        'feed_rate': random.randint(10, 1000),
        'tool_number': random.randint(1, 5),
        'coolant_status': 'ON',  # Example new attribute
        'temperature': random.uniform(20, 80),  # Simulate temperature in °C
        'power_consumption': random.uniform(100, 1000),  # Power in Watts
        'vibration_level': random.uniform(0, 5),  # Vibration in g-forces
        'tool_wear': random.uniform(0, 100),  # Percentage of tool wear
        'cycle_time': random.uniform(5, 20),  # Cycle time in seconds
        'machining_time': random.uniform(60, 180),  # Total machining time in seconds
        'unauthorized_command': random.choice([True, False]),  # Command injection anomaly
        'tool_changed': random.choice([False, True]),  # Simulate unexpected tool change
        'network_latency': random.uniform(0, 1)  # Latency in seconds
    }

def simulate_anomalies(runtime_data):
    anomaly_type = random.choice([
        'spindle_speed', 'feed_rate', 'tool_path', 'command', 'temperature', 'power', 
        'vibration', 'tool_wear', 'cycle_time', 'machining_time', 'command_injection', 
        'tool_change', 'network_latency', 'none'
    ])
    
    if anomaly_type == 'spindle_speed':
        runtime_data['spindle_speed'] = random.randint(5001, 10000)  # Out-of-range spindle speed
    elif anomaly_type == 'feed_rate':
        runtime_data['feed_rate'] = random.randint(1, 5)  # Extremely low feed rate
    elif anomaly_type == 'tool_path':
        runtime_data['coordinates'] = (random.uniform(200, 300), random.uniform(200, 300), random.uniform(200, 300))  # Unexpected coordinate shift
    elif anomaly_type == 'command':
        runtime_data['coolant_status'] = random.choice(['OFF', 'ON'])  # Unexpected coolant status change
    elif anomaly_type == 'temperature':
        runtime_data['temperature'] = random.uniform(80, 150)  # Overheating
    elif anomaly_type == 'power':
        runtime_data['power_consumption'] = random.uniform(1, 50)  # Low power consumption
    elif anomaly_type == 'vibration':
        runtime_data['vibration_level'] = random.uniform(5, 10)  # Excessive vibration
    elif anomaly_type == 'tool_wear':
        runtime_data['tool_wear'] = random.uniform(80, 100)  # High tool wear
    elif anomaly_type == 'cycle_time':
        runtime_data['cycle_time'] = random.uniform(1, 3)  # Unusually fast cycle time
    elif anomaly_type == 'machining_time':
        runtime_data['machining_time'] = random.uniform(10, 50)  # Shortened machining time
    elif anomaly_type == 'command_injection':
        runtime_data['unauthorized_command'] = True  # Command injection anomaly
    elif anomaly_type == 'tool_change':
        runtime_data['tool_changed'] = True  # Unexpected tool change
    elif anomaly_type == 'network_latency':
        runtime_data['network_latency'] = random.uniform(0.5, 2)  # High network latency

    return runtime_data

if __name__ == "__main__":
    for _ in range(10):  # Simulate 10 data points
        data = simulate_runtime_data()
        data = simulate_anomalies(data)
        print(data)


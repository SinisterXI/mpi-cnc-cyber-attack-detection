import os

def parse_gcode(file_path):
    # Open the file specified by file_path
    with open(file_path, 'r') as file:
        # Parse the G-code file
        rules = []
        for line in file:
            if "G01" in line:
                parts = line.split()
                rule = {
                    'command': parts[0],
                    'x': float(parts[1][1:]),
                    'y': float(parts[2][1:]),
                    'z': float(parts[3][1:]),
                    'feed_rate': int(parts[4][1:]),
                    'spindle_speed': int(parts[5][1:]),
                    'tool': int(parts[6][1:])
                }
                rules.append(rule)
    return rules

def detect_gcode_anomalies(gcode_rules):
    anomalies = []
    for rule in gcode_rules:
        if rule['spindle_speed'] > 5000:  # Detect spindle speed anomaly
            anomalies.append(f"Spindle speed anomaly detected in tool {rule['tool']} with speed {rule['spindle_speed']}")
        if rule['feed_rate'] < 10:  # Detect feed rate anomaly
            anomalies.append(f"Feed rate anomaly detected in tool {rule['tool']} with rate {rule['feed_rate']}")
        if rule['x'] > 100 or rule['y'] > 100 or rule['z'] > 100:  # Detect tool path anomaly
            anomalies.append(f"Tool path anomaly detected at coordinates X{rule['x']} Y{rule['y']} Z{rule['z']}")
    return anomalies

if __name__ == "__main__":
    # Path where all your G-code files are located
    gcode_directory = "/home/shameer/OS_Project/"
    
    # List all G-code files in the directory
    gcode_files = [file for file in os.listdir(gcode_directory) if file.endswith(".gcode") or file.endswith(".txt")]
    
    for gcode_file in gcode_files:
        full_path = os.path.join(gcode_directory, gcode_file)
        print(f"Checking {gcode_file} for anomalies...")
        
        # Parse the G-code file
        rules = parse_gcode(full_path)
        
        # Detect anomalies in the parsed G-code rules
        anomalies = detect_gcode_anomalies(rules)
        
        if anomalies:
            print(f"Anomalies detected in {gcode_file}:")
            print("\n".join(anomalies))
        else:
            print(f"No anomalies detected in {gcode_file}.\n")


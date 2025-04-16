# Run all scripts together
#!/bin/bash

echo "Starting CNC machine simulation..."
#python3 iot_simulation.py
python3 parse_gcode.py
python3 simulator.py
python3 detect_anomalies.py
python3 visualize.py
#python3 email_alerts.py


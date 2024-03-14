#!/bin/bash

DIR=$(pwd)

# Define the path to the Python file
python_file="$DIR/Hardware/Sensor/distance_sensors.py"

# Check if the Python file exists
if [ -f "$python_file" ]; then
    # Run the Python file
    python3 "$python_file"
else
    echo "Error: Python file not found."
    exit 1
fi

exit 0
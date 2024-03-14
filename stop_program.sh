#!/bin/bash

DIR=$(pwd)

# Define the path to the Python file
python_file="$DIR/Hardware/Sensor/distance_sensors.py"

# Check if a Python process with the given file name is running
if pgrep -f "$python_file" > /dev/null; then
    # Kill the Python process
    pkill -f "$python_file"
    echo "Python process killed."
else
    echo "No Python process with the specified file name is running."
fi

echo "Killed sensor file"

exit 0

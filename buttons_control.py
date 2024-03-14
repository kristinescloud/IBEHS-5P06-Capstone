from gpiozero import Button
import subprocess

button1 = Button(13)
button2 = Button (6)

def runStart():
    print("button1 pressed")
    # process = subprocess.Popen(["python", "distance_sensors.py"])
    subprocess.run(["bash", "start_program.sh"])
    
def runStop():
    print("button2 pressed")
    subprocess.run(["bash", "stop_program.sh"])
    
    
button1.when_pressed = runStart
button2.when_pressed = runStop
    
    
    
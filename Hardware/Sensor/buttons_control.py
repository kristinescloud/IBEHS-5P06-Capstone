from gpiozero import Button
import subprocess

button1 = Button(13)
button2 = Button (6)

def runStart():
    print("button1 pressed")
    process = subprocess.Popen(["python", "distance_sensors.py"])
    
def runStop():
    print("button2 pressed")
    process.terminate()
    
button1.when_pressed = runStart
button2.when_pressed = runStop
    
    
    
from gpiozero import DistanceSensor,PWMOutputDevice
from time import sleep


sensor1=DistanceSensor(echo=24,trigger=23,max_distance=2)
sensor2=DistanceSensor(echo=17,trigger=27,max_distance=2)
motor = PWMOutputDevice(22)

def calculate_vibration(distance):
    vibration = (-(distance-2)/198) + 1
    return vibration


while True:
    distance1 = sensor1.distance*100
    distance2 = sensor2.distance*100
    print('Distance1: ', distance1)
    print('Distance2: ', distance2)
    
    if distance1 < 20:
        print("STOP Left")
        vibration1 = calculate_vibration(distance1)
        print("vibration1", vibration1)
        motor.value = vibration1
        
    if distance2 < 20:
        print("STOP Right")
    sleep(0.5)
   
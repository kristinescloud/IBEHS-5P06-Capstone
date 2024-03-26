from gpiozero import DistanceSensor,PWMOutputDevice
from time import sleep


sensor1=DistanceSensor(echo=24,trigger=23,max_distance=2)
sensor2=DistanceSensor(echo=17,trigger=27,max_distance=2)
motor = PWMOutputDevice(22)

history1 = [0,0,0,0,0]
history2 = [0,0,0,0,0]
delta1 = [0,0,0,0]
delta2 = [0,0,0,0]

def calculate_vibration(distance):
    vibration = (-(distance-2)/198) + 1
    return vibration

while True:
    distance1 = sensor1.distance*100
    distance2 = sensor2.distance*100
    print('Distance1: ', distance1)
    print('Distance2: ', distance2)
    
    #update history
    for i in range(len(history1)-1):
        history1[i] = history1[i+1]
        history2[i] = history2[i+1]
    
    history1[-1] = distance1
    history2[-1] = distance2

    #update delta
    for i in range(len(delta1)-1):
        delta1[i] = delta1[i+1]
        delta2[i] = delta2[i+1]

    delta1 = history1[-1] - history1[-2]
    delta2 = history2[-1] - history2[-2]

    if distance1 < 20:

        if delta1 > 10:
            print("STOP Left")
            vibration1 = calculate_vibration(distance1)
            print("vibration1", vibration1)
            motor.value = vibration1
        
    if distance2 < 20:
        if delta2 > 10:
            print("STOP Right")

    sleep(0.5)
   
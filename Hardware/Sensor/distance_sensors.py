from gpiozero import DistanceSensor,PWMOutputDevice
from time import sleep


sensor1=DistanceSensor(echo=24,trigger=23,max_distance=2)
sensor2=DistanceSensor(echo=27,trigger=17,max_distance=2)
motor = PWMOutputDevice(16)
motor2 = PWMOutputDevice(12)

history1 = [0]*10
history2 = [0]*10
delta1 = [0]*9
delta2 = [0]*9
counter1 = 0
counter2 = 0

#TODO: pulsing vibration

def calculate_vibration(distance):
    vibration = 1
    #vibration = (-(distance-2)/198) + 1
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

    delta1_new = history1[-1] - history1[-2]
    delta2_new = history2[-1] - history2[-2]

    if distance1 < 20: #20cm
        counter1 += 1
        
        print("counter1:", counter1)
        print("delta1:", delta1_new)
        
        print("STOP Left")
        vibration1 = calculate_vibration(distance1)
        print("vibration1", vibration1)
        motor.value = vibration1
        
        if counter1 > 50:
            if delta1_new > -10:
                motor.value = 0
    else:
        counter1 = 0
        motor.value = 0
        
    if distance2 < 20:
        counter2 += 1
        
        print("counter2:", counter2)
        print("delta2:", delta2_new)
        
        print("STOP Right")
        vibration2 = calculate_vibration(distance2)
        print("vibration2", vibration2)
        motor2.value = vibration2
        
        if counter2 > 50:
            if delta2_new > -10:
                motor2.value = 0
    else:
        counter2 = 0
        motor2.value = 0
    

    sleep(0.1)
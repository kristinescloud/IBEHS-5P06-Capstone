import RPi.GPIO as GPIO
import time

vibration_pin = 27 # 27 was just a random number used as a placeholder and will need to be changed
GPIO.setmode(GPIO.BCM)
GPIO.setup(vibration_pin, GPIO.OUT)

def busy_wait_until(time_target_ns):
	"""
    	Busy-waits until the specified target time in nanoseconds.
    	:param target_time_ns: Target time in nanoseconds to wait until
   	 """
	while time.clock_gettime_ns(time.CLOCK_MONOTONIC) < target_time_ns:
		pass

def vibrate(pin, duration, frequency):
	"""
    	Sends a logical high for a given duration of time at a specific frequency using nanosecond precision and CLOCK_MONOTONIC.
    	:param pin: DigitalOutputPin object
    	:param duration_s: Duration in seconds for which the high signal should be maintained
    	:param frequency_hz: Frequency in Hz at which the high signal should be toggled
   	 """
	duration_ns = duration*(10**9)
	frequency_GHz = frequency/(10**9)
	period_ns = 1/frequency_GHz

	time_start_ns = clock_gettime_ns(CLOCK_MONOTONIC)
	time_end_ns = time_start_ns + duration_ns

	while clock_gettime_ns(CLOCK_MONOTONIC) < time_end_ns:
		GPIO.output(pin,GPIO.HIGH)
		busy_wait_until(clock_gettime_ns(CLOCK_MONOTONIC) + period_ns//2)
		GPIO.output(pin,GPIO.LOW)
		busy_wait_until(clock_gettime_ns(CLOCK_MONOTONIC) + period_ns//2)

	GPIO.cleanup()	

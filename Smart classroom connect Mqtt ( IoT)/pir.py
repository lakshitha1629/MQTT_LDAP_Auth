import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pirPin = 26


GPIO.setup(pirPin, GPIO.IN)

def MotionDetector(pirPin):
    
    print("Motion Detected!")
  
print("Motion Sensor Alarm (CTRL+C to exit)")
time.sleep(.2)
print("Ready")
try:
    GPIO.add_event_detect(pirPin, GPIO.RISING, callback=MotionDetector)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
 
import RPi.GPIO as GPIO
#import dht11
import adafruit_dht
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 20
instance = adafruit_dht.DHT11(20)
print("Test")

temperature = instance.temperature
humidity = instance.humidity

try:
    print("Test1")
    while True:
        
        #result = instance.read()
        if temperature is not None and humidity is not None:
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % temperature)
            print("Humidity: %-3.1f %%" % humidity)

        time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
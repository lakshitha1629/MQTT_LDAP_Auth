import RPi.GPIO as GPIO
#import dht11
import adafruit_dht
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 20
instance = adafruit_dht.DHT11(4)
print("Test")

print("Test1")

while True:
    try:
         # Print the values to the serial port
         temperature_c = instance.temperature
         temperature_f = temperature_c * (9 / 5) + 32
         humidity = instance.humidity
         print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
         time.sleep(1.0)
         
    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    
    except KeyboardInterrupt:
         print('interrupted!')
         instance.exit()
         
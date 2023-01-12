import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup (20,GPIO.OUT)#D3
GPIO.setup (21,GPIO.IN)#D4

GPIO.output(20, True)
i = 0
try:
    while True:
        if GPIO.input(21) and i == 0:
            print('button press')
            i == 1
        else:
            i == 0
except KeyboardInterrupt:
    GPIO.output(20, False)
        
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

if (GPIO.input(24)):
    print('on')
    GPIO.output(26, 1)
    time.sleep(2)
else:
    print('off')
    GPIO.output(26, 0)
    time.sleep(2)

print('end')
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

aux = [21, 20, 26, 16, 19, 25, 23, 24]
GPIO.setup(aux, GPIO.IN)

time.sleep(1)

print('begin')

while True:
    try:
        for i in range(len(leds)):
            GPIO.output(leds[i], GPIO.input(aux[i]))
    finally:
        GPIO.output(leds, 0)
        GPIO.cleanup()

        print('end')

time.sleep(1)

GPIO.output(leds, 0)
GPIO.cleanup()

print('end')
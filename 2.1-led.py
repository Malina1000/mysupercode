import RPi.GPIO as GPIO
import time

leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

print('begin')

for i in range(3):
    time.sleep(1)

    for led in leds:
        GPIO.output(led, 1)
        time.sleep(0.2)
        GPIO.output(led, 0)
        # time.sleep(0.2)

GPIO.output(leds, 0)

GPIO.cleanup()

print('end')
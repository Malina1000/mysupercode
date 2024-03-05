import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print('ATTENTION!!! LEDS ARE MANUALLY TURNED OFF')

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

while True:
    GPIO.output(leds, 0)

time.sleep(1)

GPIO.cleanup()

print('end')

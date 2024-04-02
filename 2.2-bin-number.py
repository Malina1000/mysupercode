import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)

time.sleep(1)

print('begin')

number = [0,1,1,1,1,1,1,1]
numbers = [255, 127, 64, 32, 5, 0]
GPIO.output(dac, number)
    
time.sleep(15)

GPIO.output(dac, 0)

time.sleep(1)

GPIO.cleanup()

print('end')
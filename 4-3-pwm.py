import RPi.GPIO as GPIO
import time

# =============================================== 
def DecimalToBinary(num): 
    b = [0] * 8
    i = 0
    while num: 
        if (num & 1): 
            b[i] = 1
        # if (num & 1) = 0 
        else: 
            b[i] = 0
        # right shift by 1 
        num >>= 1
        i += 1

    b.reverse()
    return b
# =============================================== 
dac = [8, 11, 7, 1, 0, 5, 12, 6]

dc = 0
GPIO.setmode (GPIO.BCM)

GPIO.setup (24, GPIO.OUT)
GPIO.setup (dac, GPIO.OUT)

p = GPIO.PWM (24, 1000)

p.start (dc)

try:
    while True:
        coeff = float (input("Fill coeff = "))
        int_c = DecimalToBinary(int(coeff / 100 * 255))
        GPIO.output(dac, int_c)
        p.ChangeDutyCycle(coeff)
        print(coeff * 3.3 / 100)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup ()

GPIO.cleanup ()
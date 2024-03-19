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

GPIO.setmode (GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)

try:
    T = int (input ("T = "))
    num = 0

    while (True):
        b = DecimalToBinary(num)
        
        GPIO.output (dac, b)
        print ('DAC voltage = ', num / 256 * 3.3)

        if (num == 255):
            flag = -1
        if (num == 0):
            flag = 1
        
        num += flag

        time.sleep(T/500)
    pass
finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()

GPIO.cleanup ()
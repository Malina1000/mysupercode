import RPi.GPIO as GPIO
import time

# =============================================== 
def DecimalToBinary(num): 
    b = [0] * 8
    i = 0
    while num: 
        if (num & 1): 
            b[i] = 1
        else: 
            b[i] = 0
        num >>= 1
        i += 1

    b.reverse()
    return b 
# =============================================== 

def adc ():
    for dec_val in range(256):
        bin_val = DecimalToBinary(dec_val)
        GPIO.output (dac, bin_val)
        comp_val = GPIO.input (comp)

        time.sleep (0.01)

        if comp_val: return dec_val
    
    return 0



dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode (GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)

try:
    while (True):
        dec_n = adc()
        volts = dec_n * 3.3 / 256
        if volts: print (volts) 

except Exception:
    print ('loser')
        
finally:
    GPIO.output (dac, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup ()

GPIO.cleanup ()




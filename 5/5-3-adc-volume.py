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
    val = 0
    for i in range(7, -1, -1):
        val += 1 << i
        
        bin_val = DecimalToBinary(val)

        GPIO.output (dac, bin_val)

        time.sleep (0.01)

        comp_val = GPIO.input (comp)

        if comp_val:
            val -= 1 << i

    return val

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode (GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)
GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup (comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

try:
    while (True):
        dec_n = adc()
        volume = []
        for i in range(len(leds)):
            if i <= dec_n / 256 * 8 and dec_n != 0:
                volume.append(1)
            else:
                volume.append(0)

        GPIO.output(leds, volume)
        volts = dec_n * 3.3 / 256
        if volts: print (round (volts, 3)) 

except Exception:
    print ('loser')
        
finally:
    GPIO.output (dac, 0)
    GPIO.output (troyka, 0)
    GPIO.cleanup ()

GPIO.cleanup ()

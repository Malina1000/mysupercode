import RPi.GPIO as GPIO

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

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode (GPIO.BCM)

GPIO.setup (dac, GPIO.OUT)

try:


    while (True):
        dec = input ('Enter number: ')
        if (dec == "q"): 
            print ("quit...")
            break
        dec = int(dec)
        if (dec < 0 or dec > 255):
            print("wrng number")
            continue
        GPIO.output (dac, DecimalToBinary (dec))

        print ('DAC voltage = ', dec / 256 * 3.3)

except Exception:
    print ('loser')
        
finally:
    GPIO.output (dac, 0)
    GPIO.cleanup ()

GPIO.cleanup ()




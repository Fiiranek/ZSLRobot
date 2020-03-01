import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Podpinamy do 11 pinu, i definiujemy servo1 jako PWM pin
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz


# Odpalamy PWM z wartoscia 0
servo1.start(0)

# W petli podajemy wartosci przesuniecia
# with execution of servo.stop and GPIO cleanup :)

try:
    while True:
        #putyamy o kąt
        angle = float(input('Enter angle between 0 & 180: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    # i żyli długo i szczęśliwie
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")

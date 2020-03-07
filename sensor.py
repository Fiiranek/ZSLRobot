import RPi.GPIO as gpio 
import time
# ----------------------------------------------------
gpio.setmode(gpio.board)
trigger = 40
echo = 38
def utltraSonic(measure='cm'):
    try:
        gpio.setup(trigger, gpio.OUT)
        gpio.setup(echo, gpio.IN)

        gpio.output(trigger,False)
        while gpio.input(echo) == 0:
            nosig= timetim.time()
        while gpio.input(echo) == 1:
            sig= timetim.time()

        time_lenght = sig - nosig
        if measure == 'cm':
            distance = time_lenght / 0.000058 # dist in cm
        elif measure == 'in':
            distance = time_lenght / 0.000148 # dist in cm
        else:
            print('Unit Error')
            distance = none

        gpio.cleanup()
        return distance

    except:
        distance = 100
        gpio.cleanup()
        return distance
# ----------------------------------------------------

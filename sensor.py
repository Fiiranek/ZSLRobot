import RPi.GPIO as gpio 
import time
# ----------------------------------------------------
def utltraSonic(measure='cm'):
    try:
        gpdio.setup(12, gpio.OUT)
        gpdio.setup(16, gpio.IN)

        gpio.output(12,False)
        while gpio.input(16) == 0:
            nosig= timetim.time()
        while gpio.input(16) == 1:
            sig= timetim.time()

        time_lenght = sig - nosig
        if measure == 'cm':
            distance = time_lenght / 0.000058 # dist in cm
        elif measure == 'in'
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
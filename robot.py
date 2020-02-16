import RPi.GPIO as gpio 
import time

import sys
import tkinter as tk

def init():
    gpio.setMode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(time):
    init()

    gpio.output(7,False)
    gpio.output(11,True)

    gpio.output(13,True)
    gpio.output(15,False)

    time.sleep(time)
    gpio.cleanup()

def backwards(time):
    init()

    gpio.output(11,False)
    gpio.output(7,True)

    gpio.output(15,True)
    gpio.output(13,False)

    time.sleep(time)
    gpio.cleanup()

def left(time):
    init()

    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)

    time.sleep(time)
    gpio.cleanup()

def right(time):
    init()

    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)

    time.sleep(time)
    gpio.cleanup()

def pivot_left(time):
    init()

    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)

    time.sleep(time)
    gpio.cleanup()

def pivot_right(time):
    init()

    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)

    time.sleep(time)
    gpio.cleanup()



# ----------------------------------------------------

def key_input(event):
    init()
    print 'Key: ', event.char
    key_press = event.char
    sleep_time = 0.03

    if key_press.lower() == 'w':
        forward(sleep_time)
    if key_press.lower() == 's':
        backwards(sleep_time)
    if key_press.lower() == 'a':
        left(sleep_time)
    if key_press.lower() == 'd':
        right(sleep_time)    

# pivots
    if key_press.lower() == 'q':
        pivot_left(sleep_time)
    if key_press.lower() == 'e':
        pivot_right(sleep_time)
    else:
        pass 

# ----------------------------------------------------
def utltraSonic(measure='cm'):
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

# ----------------------------------------------------

command = tk.Tk()
command.bind('<key_press',key_input)
command.mainloop()

# def main():
#     # forward(5)
#     # left(5)





if __name__ == '__main__':
    main()

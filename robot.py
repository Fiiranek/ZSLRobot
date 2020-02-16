import RPi.GPIO as gpio 
import time



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

def main():
    forward(5)
    left(5)





if __name__ == '__main__':
    main()

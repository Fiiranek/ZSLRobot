import RPi.GPIO as gpio 
import time
import bluetooth

import sys
import tkinter as tk

from sensor import utltraSonic


# Komunikacja via niebieskiego zęba
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_socket.bind(("", port))
server_socket.listen(1)

# https://github.com/vishalavalani/Raspberry-Pi-Robotics/blob/master/Raspberry%20Pi%20Robot%20controlled%20by%20Android%20App%20via%20Bluetooth/bluetoothrobot
# https://github.com/vishalavalani/Raspberry-Pi-Robotics/tree/master/Raspberry%20Pi%20Robot%20controlled%20by%20Android%20App%20via%20Bluetooth

client_socket, address = server_socket.accept()
print "Accepted connection from ", address

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

def break(time):
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,True)

    time.sleep(time)
    gpio.cleanup()

def BluetoothControll():
    try:
        while 1:
            data = client_socket.recv(1024)
            print "Received: %s" % data
            if (data == "0"):
                break()
                print("Break")
            if (data == "1"):
                forward()
                print("Forward")
            if (data == "2"):
                backwards()
                print("Reverse")
            if (data == "3"):
                print("Left")
                for x in range(1, 3 , 1):
                    left()
                    time.sleep(0.1)
                break()
            if (data == "4"):
                print("Right")
                for x in range(1, 3 , 1):
                    right()
                    time.sleep(0.1)
                break()
            if (data == "q"):
                break()
                print("Brake")
                print ("Quit")
                break

    finally:
        print("Cleaning Up!")
        GPIO.cleanup()
        client_socket.close()
        server_socket.close()
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

# getting ultrasonic sensor values
    currDist = utltraSonic('cm')
    if currDist < 20:
        init()
        backwards(2)

command = tk.Tk()
command.bind('<key_press',key_input)
command.mainloop()

# def main():
#     # forward(5)
#     # left(5)


client_socket.close()
server_socket.close()


if __name__ == '__main__':
    main()

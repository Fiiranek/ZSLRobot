# import curses and GPIO
import curses
import RPi.GPIO as GPIO
from mpu6050 import mpu6050
import time
import os
GPIO.setwarnings(False)

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)

motor1a = 7
motor1b = 11
mpu = mpu6050(0x68)
motor2a = 13
motor2b = 16
GPIO.cleanup()
GPIO.setup(motor1a,GPIO.OUT)
GPIO.setup(motor1b,GPIO.OUT)
GPIO.setup(motor2a,GPIO.OUT)
GPIO.setup(motor2b,GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
pwm=GPIO.PWM(21, 50)
pwm.start(0)
def SetAngle(angle):
        duty = angle / 18 + 2
        GPIO.output(21, True)
        pwm.ChangeDutyCycle(duty)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)
GPIO.output(motor1a,GPIO.LOW)
GPIO.output(motor1b,GPIO.LOW)
GPIO.output(motor2a,GPIO.LOW)
GPIO.output(motor2b,GPIO.LOW)

SetAngle(90)
try:
        while True:
                os.system('clear')
                print("Temp : "+str(round(mpu.get_temp(),2)))

                accel_data = mpu.get_accel_data()
                print("Acc X : "+str(round(accel_data['x'],2)))
                print("Acc Y : "+str(round(accel_data['y'],2)))
                print("Acc Z : "+str(round(accel_data['z'],2)))

                gyro_data = mpu.get_gyro_data()
                print("Gyro X : "+str(round(gyro_data['x'],2)))
                print("Gyro Y : "+str(round(gyro_data['y'],2)))
                print("Gyro Z : "+str(round(gyro_data['z'],2)))
                time.sleep(0.1)
                char = screen.getch()
                oldChar = char
                if char == ord('q'):
                        break
                elif char == curses.KEY_RIGHT:
                        GPIO.output(motor1a,GPIO.HIGH)
                        GPIO.output(motor1b,GPIO.LOW)
                        GPIO.output(motor2a,GPIO.HIGH)
                        GPIO.output(motor2b,GPIO.LOW)
                elif char == ord('a'):
                        SetAngle(180)
                elif char == ord('d'):
                        SetAngle(0)
                elif char == ord('s'):
                        SetAngle(90)
                elif char == curses.KEY_LEFT:
                        GPIO.output(motor1a,GPIO.LOW)
                        GPIO.output(motor1b,GPIO.HIGH)
                        GPIO.output(motor2a,GPIO.LOW)
                        GPIO.output(motor2b,GPIO.HIGH)
                elif char == curses.KEY_UP:
                        GPIO.output(motor1a,GPIO.HIGH)
                        GPIO.output(motor1b,GPIO.LOW)
                        GPIO.output(motor2a,GPIO.LOW)
                        GPIO.output(motor2b,GPIO.HIGH)
                elif char == curses.KEY_DOWN:
                        GPIO.output(motor1a,GPIO.LOW)
                        GPIO.output(motor1b,GPIO.HIGH)
                        GPIO.output(motor2a,GPIO.HIGH)
                        GPIO.output(motor2b,GPIO.LOW)
                else:
                        GPIO.output(21, True)
                        pwm.ChangeDutyCycle(0)
                        GPIO.output(motor1a,GPIO.LOW)
                        GPIO.output(motor1b,GPIO.LOW)
                        GPIO.output(motor2a,GPIO.LOW)
                        GPIO.output(motor2b,GPIO.LOW)
finally:
    #Close down curses properly, inc turn echo back on!
        SetAngle(90)
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        GPIO.cleanup()

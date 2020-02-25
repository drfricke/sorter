#EV3 code 02/24/20

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Write your program here

#start up stuff
from pybricks.parameters import Color, Port
from pybricks.iodevices import AnalogSensor, UARTDevice
uart = UARTDevice(Port.S1, 9600, timeout=2000)
#uart.write("HelloRpi".encode()) 

#ev3 waits for UART byte - once it sees, it reads it

placer = Motor(Port.A)
trash = Motor(Port.B)
redDudes = Motor(Port.C)

valIfRed = 1 #value pi sends if the brick is red (placeholder)
valIfNotRed = 0 #value pi sends if the brick is not red (placeholder) 

placedTarget = 0 #angle value for placer to position brick under camera (placeholder)
placerwaiting = -120 #angle value for placer in the waiting for brick position (placeholder)

redAngleTarget = 300 #angle value for red mover to move red bricks to cup (placeholder)
redStartAngle = 0 #rest position angle for red mover

trashStartingAngle = 0 #waiting angle for trash mover (placeholder)
trashchuckAngle = 50 #moving angle for trash mover (placeholder)

while True:
    #to use: place a brick in the mover and then push the center button

    #if center button is pushed, move brick to sensing position and send something to pi to tell it to read
    if button.CENTER in brick.buttons():
        placer.run_target(300, placedTarget, Stop.BRAKE, True) #target angle placeholder for now
        uart.write("r".encode()) #placeholder value

    if uart.waiting() >= 1:
        data = uart.read(1)
        print(data.decode('utf-8'))
        #if red, put in red bin
        if data == valIfRed:

            #might need to change these to run_angles depending on arm style
            redDudes.run_target(300, redAngleTarget, Stop.BRAKE, True)
            redDudes.run_target(300, redStartAngle, Stop.BRAKE, True) #reset the red mover arm
        
        #if not red, throw brick away
        if data == valIfNotRed:
            #might need to change these to run_angles depending on arm style
            trash.run_target(300, trashchuckAngle, Stop.BRAKE, True)
            trash.run_target(300, trashStartingAngle, Stop.BRAKE, True)
        
        #return brick placer to 'waiting' position
        placer.run_target(300, placerwaiting, Stop.BRAKE, True)

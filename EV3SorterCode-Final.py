#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Write your program here

#start up stuff- Ports, Comm, int motors/sensors
from pybricks.parameters import Color, Port
from pybricks.iodevices import AnalogSensor, UARTDevice
uart = UARTDevice(Port.S1, 9600, timeout=2000)

beltmotor = Motor(Port.A)
booter = Motor(Port.B)
button = TouchSensor(Port.S4)


#ev3 waits for UART byte - once it sees, it reads it
# 1st if: checks to see if one byte is on the buffer connection
  # Nested ifs: If red uses piston to knock piece off
                #if not: Keeps moving the belt
  # Last if corrects piston, Sometimes the encoder drifts/friction in the actual system prevent proper correction. Minor though.

while True:
    if uart.waiting() >= 1:
        data = uart.read(1)
        #print(data.decode('utf-8'))
        if data.decode('utf-8') == 'y':
            print('red')
            booter.run_target(350,350)
            booter.reset_angle(0)
        if data.decode('utf-8') == 'n':
            print('moving')
            beltmotor.run_time(300,150)
    if button.pressed():
        booter.run_target(100,20)
        booter.reset_angle(0)



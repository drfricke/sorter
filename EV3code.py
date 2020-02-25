#EV3 code 02/24/20

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
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

while True:
    if uart.waiting() >= 1:
        data = uart.read(1)
        print(data.decode('utf-8'))
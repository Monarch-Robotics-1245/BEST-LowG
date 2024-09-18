#!/usr/bin/env python3

import subsystems.drivetrain
import autos.auto
import subsystems.servo


def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, previousServoOne):

    leftMotor = 0
    rightMotor = 0 # max declared is 127
    motorOne = 0
    motorTwo = 0
    servoOne = 0
    servoTwo = 0
    servoThree = 0
    servoFour = 0
    # 0 (not pressed) and 1(pressed) - not True and False for buttons
    subsystems.drivetrain.drive(axisTwo, axisThree)
    autos.auto.auto()
    subsystems.servo.servo(eightU, eightD, previousServoOne)
    # call functions here
    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour

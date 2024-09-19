#!/usr/bin/env python3

import commands.drivetrain


def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, previousEightR, previousEightL, leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier):

    # Constants
    SLOW_SPEED = .25
    FAST_SPEED = 1

    # 0 (not pressed) and 1(pressed) - not True and False for buttons
    commands.drivetrain.drive(direction, speedMultiplier, axisOne, axisTwo, eightR, eightL, previousEightR, previousEightL, SLOW_SPEED, FAST_SPEED)

    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier

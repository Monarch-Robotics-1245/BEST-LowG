#!/usr/bin/env python3

# Standard Declaration
# leftMotor = 0
# rightMotor = 0
# motorOne = 0
# motorTwo = 0
# servoOne = 0
# servoTwo = 0
# servoThree = 0
# servoFour = 0
# axisOne = 0
# axisTwo = 0
# axisThree = 0
# axisFour = 0
# fiveU = 0
# fiveD = 0
# sixU = 0
# sixD = 0
# sevenU = 0
# sevenL = 0
# sevenR = 0
# sevenD = 0
# eightR = 0
# eightD = 0
# eightU = 0
# eightL = 0
# End Standard Declaration

import subsystems.drivetrain
import constants.drivetrain


def drive(driveFwd, driveSide, reverseButton, previousReverseButton, direction, speedMultiplier, speedButton, previousSpeedButton):
    """
    
    Takes in the joystick values and sets the motors to the correct values.
    
    direction (int): 1 is backwards, 0 is forwards
    speedMultiplier (int): current speed multiplier for the robot
    axisOne (int): Joystick Axis 1
    axisTwo (int): Joystick Axis 2
    eightR (int): Joystick Button 8 Right
    eightL (int): Joystick Button 8 Left
    previousEightR (int): Joystick Button 8 Right Previous
    previousEightL (int): Joystick Button 8 Left Previous
    """
    left = driveFwd + driveSide
    right = driveFwd - driveSide

    if previousReverseButton == 1 and reverseButton == 0:
        if direction == 0:
            direction = 1
        else:
            direction = 0

    if previousSpeedButton == 1 and speedButton == 0:
        if speedMultiplier == constants.drivetrain.FAST_SPEED:
            speedMultiplier = constants.drivetrain.SLOW_SPEED
        else:
            speedMultiplier = constants.drivetrain.FAST_SPEED
    left = left * speedMultiplier
    right = right * speedMultiplier
    if direction == 1:
        left = -left
        right = -right

    # 1 is backwards, 0 is forwards
    subsystems.drivetrain.setLeftMotor(left)
    subsystems.drivetrain.setRightMotor(right)
    
    
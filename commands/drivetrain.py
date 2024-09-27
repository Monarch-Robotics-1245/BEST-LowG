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

def drive(direction, speedMultiplier, axisOne, axisTwo, eightR, eightL, previousEightR, previousEightL):
    """
    Takes in the joystick values and sets the motors to the correct values

    :param direction: int - 1 is backwards, 0 is forwards
    :param speedMultiplier: int - current speed multiplier for the robot
    :param axisOne: int - Joystick Axis 1
    :param axisTwo: int - Joystick Axis 2
    :param eightR: int - Joystick Button 8 Right
    :param eightL: int - Joystick Button 8 Left
    :param previousEightR: int - Joystick Button 8 Right Previous
    :param previousEightL: int - Joystick Button 8 Left Previous
    :return: 
    """
    
    left = axisOne + axisTwo
    right = axisOne - axisTwo
    
    # 1 is backwards, 0 is forwards
    if previousEightR == 1 and eightR == 0:
        if direction == 0:
            direction = 1
        else:
            direction = 0


    if previousEightL == 1 and eightL == 0:
        if speedMultiplier == constants.drivetrain.FAST_SPEED:
            speedMultiplier = constants.drivetrain.SLOW_SPEED
        else:
            speedMultiplier = constants.drivetrain.FAST_SPEED
    
    left = left * speedMultiplier
    right = right * speedMultiplier
    
    if direction == 1:
        left = -left
        right = -right
    
    subsystems.drivetrain.setLeftMotor(left)
    subsystems.drivetrain.setRightMotor(right)
    
    
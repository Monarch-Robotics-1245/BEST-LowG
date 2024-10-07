#!/usr/bin/env python3

import commands


def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, analogOne, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, lastPosition, lastPositionSet, previousSevenU, previousSevenL, previousEightR, previousEightL, leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier):
    """
    This function is the main function that calls all of the other functions in the commands folder. It is the main
    function that the robot will run. It will take in all of the inputs from the robot and then run the functions
    accordingly.
    :param axisOne: The first axis of the controller
    :param axisTwo: The second axis of the controller
    :param axisThree: The third axis of the controller
    :param axisFour: The fourth axis of the controller
    :param fiveU: The fifth button of the controller
    :param fiveD: The sixth button of the controller
    :param sixU: The seventh button of the controller
    :param sixD: The eighth button of the controller
    :param sevenU: The ninth button of the controller
    :param sevenL: The tenth button of the controller
    :param sevenR: The eleventh button of the controller
    :param sevenD: The twelfth button of the controller
    :param eightR: The thirteenth button of the controller
    :param eightD: The fourteenth button of the controller
    :param eightU: The fifteenth button of the controller
    :param eightL: The sixteenth button of the controller
    :param analogOne: The first analog stick of the controller
    :param digitalOne: The first digital button of the controller
    :param digitalTwo: The second digital button of the controller
    :param digitalThree: The third digital button of the controller
    :param digitalFour: The fourth digital button of the controller
    :param digitalFive: The fifth digital button of the controller
    :param lastPosition: The last position of the tower
    :param lastPositionSet: The last position set of the tower
    :param previousSevenU: The previous position of the seventh button
    :param previousSevenL: The previous position of the tenth button
    :param previousEightR: The previous position of the thirteenth button
    :param previousEightL: The previous position of the sixteenth button
    :param leftMotor: The left motor of the robot
    :param rightMotor: The right motor of the robot
    :param motorOne: The first motor of the robot
    :param motorTwo: The second motor of the robot
    :param servoOne: The first servo of the robot
    :param servoTwo: The second servo of the robot
    :param servoThree: The third servo of the robot
    :param servoFour: The fourth servo of the robot
    :param direction: The direction of the robot
    :param speedMultiplier: The speed multiplier of the robot
    :return: The left motor, right motor, first motor, second motor, first servo, second servo, third servo, fourth servo,
    """
    # 0 (not pressed) and 1(pressed) - not True and False for buttons
    commands.drivetrain.drive(direction, speedMultiplier, axisOne, axisTwo, eightR, eightL, previousEightR, previousEightL)
    commands.drawBridge.runDrawBridge(servoThree, sevenU, sevenL, previousSevenU, previousSevenL)
    commands.gripper.gripper(servoFour, fiveU, fiveD, sixU, sixD)
    commands.tower.moveTower(motorTwo, axisFour, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, lastPosition, lastPositionSet)
    commands.turret.rotateTurret(axisThree, motorOne, analogOne)
    commands.wrist.moveWrist(fiveD, fiveU, servoTwo)

    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier, lastPosition, lastPositionSet

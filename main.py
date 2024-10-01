#!/usr/bin/env python3

import commands


def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR,
          eightD, eightU, eightL, analogOne, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive,
          lastPosition, lastPositionSet, previousSevenU, previousSevenL, previousEightR, previousEightL, leftMotor,
          rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier):

    # 0 (not pressed) and 1(pressed) - not True and False for buttons
    commands.drivetrain.drive(direction, speedMultiplier, axisOne, axisTwo, eightR, eightL, previousEightR,
                              previousEightL)
    commands.drawBridge.runDrawBridge(servoThree, sevenU, sevenL, previousSevenU, previousSevenL)
    commands.gripper.gripper(servoFour, fiveU, fiveD, sixU, sixD)
    commands.tower.moveTower(motorTwo, axisFour, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive,
                             lastPosition, lastPositionSet)
    commands.turret.rotateTurret(axisThree, motorOne, analogOne)
    commands.wrist.moveWrist(fiveD, fiveU, servoTwo)

    return (leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction,
            speedMultiplier, lastPosition, lastPositionSet)

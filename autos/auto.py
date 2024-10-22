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

import subsystems
import constants

def auto(autoStage, digitalSix, digitalSeven, analogOne, lastPosition, lastPositionSet, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, autoID):
    if autoStage == 1:
        subsystems.tower.setTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, constants.auto.TOWER_START, lastPosition, lastPositionSet)

        if autoID == 1:
            subsystems.turret.setTurretRotation(analogOne, constants.auto.TURRET_START_A)
        elif autoID == 2:
            subsystems.turret.setTurretRotation(analogOne, constants.auto.TURRET_START_B)
        subsystems.gripper.setGripper(constants.auto.GRIPPER_OPEN)
        subsystems.wrist.setWrist(constants.auto.WRIST_START)
        if analogOne == constants.auto.TURRET_ROTATION and digitalFour == 1:
            autoStage = 2

    elif autoStage == 2:
        subsystems.drivetrain.setLeftMotor(constants.auto.BACK_SPEED)
        subsystems.drivetrain.setRightMotor(constants.auto.BACK_SPEED)
        if digitalSix == 1 and digitalSeven == 1:
            subsystems.drivetrain.setLeftMotor(0)
            subsystems.drivetrain.setRightMotor(0)
            autoStage = 3
    elif autoStage == 3:
        subsystems.wrist.setWrist(constants.auto.WRIST_END)
        autoStage = 4
    elif autoStage == 4:
        subsystems.tower.setTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, constants.auto.TOWER_MIDDLE, lastPosition, lastPositionSet)
        if digitalThree == 1:
            autoStage = 5
    elif autoStage == 5:
        subsystems.gripper.setGripper(constants.auto.GRIPPER_CLOSE)
        autoStage = 6
    elif autoStage == 6:
        subsystems.tower.setTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, constants.auto.TOWER_END, lastPosition, lastPositionSet)
        if digitalFour == 1:
            autoStage = 7
    elif autoStage == 7:
        subsystems.drivetrain.setLeftMotor(constants.auto.FWD_SPEED)
        subsystems.drivetrain.setRightMotor(constants.auto.FWD_SPEED)



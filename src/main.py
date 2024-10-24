#!/usr/bin/env python3

import src.commands.drivetrain
import src.commands.drawBridge
import src.commands.gripper
import src.commands.tower
import src.commands.turret
import src.commands.wrist
import src.commands
import src.subsystems
import src.constants
import src.autos

def robot(leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, digitalSix, digitalSeven, digitalEight, digitalNine, driveFwd, driveSide, dbgUp, dbgDown, previousDbgDown, previousDbgUp, grip, release, previousGrip, previousRelease, towerAxis, lastPosition, lastPositionSet, turretAxis, analogOne, wristDown, wristUp, previousWristDown, previousWristUp, turretUp, previousTurretUp, previousTurretDown, turretDown, modeToggle, previousModeToggle, state, targetPosition, autoAButton, previousAutoAButton, autoBButton, previousAutoBButton, autoID, reverseButton, previousReverseButton, speedButton, previousSpeedButton, speedMultiplier, direction, autoStage):
    # 0 (not pressed) and 1(pressed) - not True and False for buttons

    #if ok
    if digitalEight == 1:
        allowedStates = 1
    else:
        allowedStates = 0.

    if autoAButton == 1 and previousAutoAButton == 0:
        autoID = 1
    elif autoBButton == 1 and previousAutoBButton == 0:
        autoID = 2

    if allowedStates == 1:
        if modeToggle == 0 & previousModeToggle == 1:
            if state == 1:
                state = 2
                autoStage = 1
            elif state == 2:
                state = 1
    elif allowedStates == 0:
        state = 0

    if state == 0:
        src.commands.drivetrain.drive(driveFwd, driveSide, reverseButton, previousReverseButton, direction, speedMultiplier, speedButton, previousSpeedButton)
        src.commands.drawBridge.runDrawBridge(dbgUp, dbgDown, previousDbgUp, previousDbgDown)
        src.commands.gripper.gripper(grip, release, previousGrip, previousRelease)
        src.commands.tower.moveTower(towerAxis, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive,
                                     lastPosition, lastPositionSet)
        src.commands.turret.rotateTurret(turretAxis, analogOne)
        src.commands.wrist.moveWrist(wristDown, wristUp, previousWristDown, previousWristUp)
    elif state == 1:
        src.autos.auto.auto(autoStage, digitalSix, digitalSeven, analogOne, lastPosition, lastPositionSet, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, autoID)
    elif state == 2:
        src.commands.drivetrain.drive(driveFwd, driveSide, leftMotor, rightMotor)
        src.commands.drawBridge.runDrawBridge(dbgUp, dbgDown, previousDbgUp, previousDbgDown)
        src.commands.gripper.gripper(grip, release, previousGrip, previousRelease)
        src.commands.turret.rotateTurret(turretAxis, analogOne)
        src.commands.wrist.moveWrist(wristDown, wristUp, previousWristDown, previousWristUp, servoTwo)

        if turretUp == 1 & previousTurretUp:
            targetPosition = lastPosition + 1
        elif turretDown == 1 & previousTurretDown:
            targetPosition = lastPosition - 1

        if targetPosition == 0:
            src.commands.tower.moveTower(towerAxis, digitalOne, digitalTwo, digitalThree, digitalFour,
                                         digitalFive, lastPosition, lastPositionSet)
        else:
            src.subsystems.tower.setTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive,
                                                  targetPosition, lastPosition, lastPositionSet)


    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, lastPosition, lastPositionSet, targetPosition, autoID, direction, speedMultiplier, autoStage

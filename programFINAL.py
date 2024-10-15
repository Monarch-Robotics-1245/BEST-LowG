def robot(leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, digitalSix, digitalSeven, digitalEight, digitalNine, driveFwd, driveSide, dbgUp, dbgDown, previousDbgDown, previousDbgUp, grip, release, previousGrip, previousRelease, towerAxis, lastPosition, lastPositionSet, turretAxis, analogOne, wristDown, wristUp, previousWristDown, previousWristUp, turretUp, previousTurretUp, previousTurretDown, turretDown, modeToggle, previousModeToggle, state, targetPosition, autoAButton, previousAutoAButton, autoBButton, previousAutoBButton, autoID, reverseButton, previousReverseButton, speedButton, previousSpeedButton, speedMultiplier, direction, autoStage):
    DRAWBRIDGE_OPEN = 127
    DRAWBRIDGE_CLOSE = -127
    DRIVETRAIN_SLOW_SPEED = .25
    DRIVETRAIN_FAST_SPEED = 1
    GRIPPER_OPEN = 127
    GRIPPER_CLOSE = -127
    TOWER_SPEED = 100
    TURRET_UPPER_LIMIT = 100
    TURRET_LOWER_LIMIT = -100
    TURRET_SLOW_ROTATE_SPEED = 40
    TURRET_FAST_ROTATE_SPEED = 100
    TURRET_DEAD_ZONE = 5
    TURRET_SLOW_ZONE = 10
    TURRET_ANGLE_CONVERSION = 1
    WRIST_ROTATE_INCREMENT = 10
    AUTO_TOWER_START = 0
    AUTO_TURRET_START_A = 0
    AUTO_TURRET_START_B = 0
    AUTO_GRIPPER_OPEN = 0
    AUTO_WRIST_START = 0
    AUTO_TURRET_ROTATION = 0
    AUTO_BACK_SPEED = 0
    AUTO_WRIST_END = 0
    AUTO_TOWER_MIDDLE = 0
    AUTO_GRIPPER_CLOSE = 0
    AUTO_TOWER_END = 0
    AUTO_FWD_SPEED = 0

    # 0 (not pressed) and 1(pressed) - not True and False for buttons
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
        left = driveFwd + driveSide
        right = driveFwd - driveSide

        if previousReverseButton == 1 and reverseButton == 0:
            if direction == 0:
                direction = 1
            else:
                direction = 0

        if previousSpeedButton == 1 and speedButton == 0:
            if speedMultiplier == DRIVETRAIN_FAST_SPEED:
                speedMultiplier = DRIVETRAIN_SLOW_SPEED
            else:
                speedMultiplier = DRIVETRAIN_FAST_SPEED
        left = left * speedMultiplier
        right = right * speedMultiplier
        if direction == 1:
            left = -left
            right = -right

        # 1 is backwards, 0 is forwards
        leftMotor = left
        rightMotor = right

        if dbgUp == 1 and previousDbgUp == 0:
            servoThree = DRAWBRIDGE_OPEN

        elif dbgDown == 1 and previousDbgDown == 0:
            servoThree = DRAWBRIDGE_CLOSE

        if release == 1 and previousRelease == 0:
            servoOne = GRIPPER_OPEN
        elif grip == 1 and previousGrip == 0:
            servoOne = GRIPPER_CLOSE

        if digitalOne == 1:
            lastPosition = 0
            lastPositionSet = 1
        elif digitalTwo == 1:
            lastPosition = 4
            lastPositionSet = 1
        elif digitalThree == 1:
            lastPosition = 1
            lastPositionSet = 1
        elif digitalFour == 1:
            lastPosition = 2
            lastPositionSet = 1
        elif digitalFive == 1:
            lastPosition = 3
            lastPositionSet = 1
        elif lastPositionSet == 0:
            lastPosition = 4
            lastPositionSet = 1

        if digitalOne == 1:
            if towerAxis > 0:
                motorTwo = towerAxis
            else:
                motorTwo = 0
        elif digitalTwo == 1:
            if towerAxis > 0:
                motorTwo = towerAxis
            else:
                motorTwo = 0
        else:
            motorTwo = towerAxis

        if analogOne > TURRET_UPPER_LIMIT:
            if 0 > turretAxis:
                motorOne = turretAxis
            else:
                motorOne = 0
        elif analogOne < TURRET_LOWER_LIMIT:
            if 0 < turretAxis:
                motorOne = turretAxis
            else:
                motorOne = 0
        else:
            motorOne = turretAxis

        if wristUp == 1 and previousWristUp == 1:
            servoTwo += WRIST_ROTATE_INCREMENT
        elif wristDown == 1 and previousWristDown == 1:
            servoTwo -= WRIST_ROTATE_INCREMENT

    elif state == 1:
        if autoStage == 1:
            if digitalOne == 1:
                lastPosition = 0
                lastPositionSet = 1
            elif digitalTwo == 1:
                lastPosition = 4
                lastPositionSet = 1
            elif digitalThree == 1:
                lastPosition = 1
                lastPositionSet = 1
            elif digitalFour == 1:
                lastPosition = 2
                lastPositionSet = 1
            elif digitalFive == 1:
                lastPosition = 3
                lastPositionSet = 1
            elif lastPositionSet == 0:
                lastPosition = 4
                lastPositionSet = 1

            if AUTO_TOWER_START == 1:
                if digitalOne == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 0:
                    motorTwo = -1 * TOWER_SPEED
                elif lastPosition < 0:
                    motorTwo = TOWER_SPEED
            if AUTO_TOWER_START == 2:
                if digitalThree == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 1:
                    motorTwo = -1 * TOWER_SPEED
                elif lastPosition < 1:
                    motorTwo = TOWER_SPEED
            if AUTO_TOWER_START == 3:
                if digitalFour == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 2:
                    motorTwo = -1 * TOWER_SPEED
                elif lastPosition < 2:
                    motorTwo = TOWER_SPEED
            if AUTO_TOWER_START == 4:
                if digitalFive == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 3:
                    motorTwo = -1 * TOWER_SPEED
                elif lastPosition < 3:
                    motorTwo = TOWER_SPEED
            if AUTO_TOWER_START == 5:
                if digitalTwo == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 4:
                    motorTwo = -1 * TOWER_SPEED
                elif lastPosition < 4:
                    motorTwo = TOWER_SPEED
                else:
                    motorTwo = TOWER_SPEED

            if autoID == 1:
                AUTO_TURRET_START_A *= TURRET_ANGLE_CONVERSION
                if analogOne + TURRET_SLOW_ZONE > AUTO_TURRET_START_A:
                    motorOne = TURRET_FAST_ROTATE_SPEED
                elif analogOne - TURRET_SLOW_ZONE < AUTO_TURRET_START_A:
                    motorOne = -1 * TURRET_FAST_ROTATE_SPEED
                elif analogOne + TURRET_DEAD_ZONE > AUTO_TURRET_START_A:
                    motorOne = TURRET_SLOW_ROTATE_SPEED
                elif analogOne - TURRET_DEAD_ZONE < AUTO_TURRET_START_A:
                    motorOne = -1 * TURRET_SLOW_ROTATE_SPEED
                else:
                    motorOne = 0
            elif autoID == 2:
                AUTO_TURRET_START_B *= TURRET_ANGLE_CONVERSION
                if analogOne + TURRET_SLOW_ZONE > AUTO_TURRET_START_B:
                    motorOne = TURRET_FAST_ROTATE_SPEED
                elif analogOne - TURRET_SLOW_ZONE < AUTO_TURRET_START_B:
                    motorOne = -1 * TURRET_FAST_ROTATE_SPEED
                elif analogOne + TURRET_DEAD_ZONE > AUTO_TURRET_START_B:
                    motorOne = TURRET_SLOW_ROTATE_SPEED
                elif analogOne - TURRET_DEAD_ZONE < AUTO_TURRET_START_B:
                    motorOne = -1 * TURRET_SLOW_ROTATE_SPEED
                else:
                    motorOne = 0
            servoOne = AUTO_GRIPPER_OPEN
            servoTwo = AUTO_WRIST_START
            if analogOne == AUTO_TURRET_ROTATION and digitalFour == 1:
                autoStage = 2

        elif autoStage == 2:
            leftMotor = AUTO_BACK_SPEED
            rightMotor = AUTO_BACK_SPEED
            if digitalSix == 1 and digitalSeven == 1:
                leftMotor = 0
                rightMotor = 0
                autoStage = 3
        elif autoStage == 3:
            servoTwo = AUTO_WRIST_END
            autoStage = 4
        elif autoStage == 4:
            if digitalOne == 1:
                lastPosition = 0
                lastPositionSet = 1
            elif digitalTwo == 1:
                lastPosition = 4
                lastPositionSet = 1
            elif digitalThree == 1:
                lastPosition = 1
                lastPositionSet = 1
            elif digitalFour == 1:
                lastPosition = 2
                lastPositionSet = 1
            elif digitalFive == 1:
                lastPosition = 3
                lastPositionSet = 1
            elif lastPositionSet == 0:
                lastPosition = 4
                lastPositionSet = 1

            if AUTO_TOWER_MIDDLE == 1:
                if digitalOne == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 0:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 0:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_MIDDLE == 2:
                if digitalThree == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 1:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 1:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_MIDDLE == 3:
                if digitalFour == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 2:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 2:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_MIDDLE == 4:
                if digitalFive == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 3:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 3:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_MIDDLE == 5:
                if digitalTwo == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 4:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 4:
                    motorTwo =  TOWER_SPEED
                else:
                    motorTwo =  TOWER_SPEED

            if digitalThree == 1:
                autoStage = 5
        elif autoStage == 5:
            servoOne = AUTO_GRIPPER_CLOSE
            autoStage = 6
        elif autoStage == 6:
            if digitalOne == 1:
                lastPosition = 0
                lastPositionSet = 1
            elif digitalTwo == 1:
                lastPosition = 4
                lastPositionSet = 1
            elif digitalThree == 1:
                lastPosition = 1
                lastPositionSet = 1
            elif digitalFour == 1:
                lastPosition = 2
                lastPositionSet = 1
            elif digitalFive == 1:
                lastPosition = 3
                lastPositionSet = 1
            elif lastPositionSet == 0:
                lastPosition = 4
                lastPositionSet = 1

            if AUTO_TOWER_END == 1:
                if digitalOne == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 0:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 0:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_END == 2:
                if digitalThree == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 1:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 1:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_END == 3:
                if digitalFour == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 2:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 2:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_END == 4:
                if digitalFive == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 3:
                    motorTwo = -1 * TOWER_SPEED
                elif lastPosition < 3:
                    motorTwo =  TOWER_SPEED
            if AUTO_TOWER_END == 5:
                if digitalTwo == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 4:
                    motorTwo =  -1 * TOWER_SPEED
                elif lastPosition < 4:
                    motorTwo =  TOWER_SPEED
                else:
                    motorTwo =  TOWER_SPEED

            if digitalFour == 1:
                autoStage = 7
        elif autoStage == 7:
            leftMotor = AUTO_FWD_SPEED
            rightMotor = AUTO_FWD_SPEED

    elif state == 2:


        left = driveFwd + driveSide
        right = driveFwd - driveSide

        if previousReverseButton == 1 and reverseButton == 0:
            if direction == 0:
                direction = 1
            else:
                direction = 0

        if previousSpeedButton == 1 and speedButton == 0:
            if speedMultiplier == 1:
                speedMultiplier = .25
            else:
                speedMultiplier = 1
        left = left * speedMultiplier
        right = right * speedMultiplier
        if direction == 1:
            left = -left
            right = -right

        # 1 is backwards, 0 is forwards
        leftMotor = left
        rightMotor = right

        if dbgUp == 1 and previousDbgUp == 0:
            servoThree = DRAWBRIDGE_OPEN

        elif dbgDown == 1 and previousDbgDown == 0:
            servoThree = DRAWBRIDGE_CLOSE

        if release == 1 and previousRelease == 0:
            servoOne = GRIPPER_OPEN
        elif grip == 1 and previousGrip == 0:
            servoOne = GRIPPER_CLOSE

        if analogOne > TURRET_UPPER_LIMIT:
            if 0 > turretAxis:
                motorOne = turretAxis
            else:
                motorOne = 0
        elif analogOne < TURRET_LOWER_LIMIT:
            if 0 < turretAxis:
                motorOne = turretAxis
            else:
                motorOne = 0
        else:
            motorOne = turretAxis

        if wristUp == 1 and previousWristUp == 1:
            servoTwo += WRIST_ROTATE_INCREMENT
        elif wristDown == 1 and previousWristDown == 1:
            servoTwo -= WRIST_ROTATE_INCREMENT

        if turretUp == 1 & previousTurretUp:
            targetPosition = lastPosition + 1
        elif turretDown == 1 & previousTurretDown:
            targetPosition = lastPosition - 1

        if targetPosition == 0:
            if digitalOne == 1:
                lastPosition = 0
                lastPositionSet = 1
            elif digitalTwo == 1:
                lastPosition = 4
                lastPositionSet = 1
            elif digitalThree == 1:
                lastPosition = 1
                lastPositionSet = 1
            elif digitalFour == 1:
                lastPosition = 2
                lastPositionSet = 1
            elif digitalFive == 1:
                lastPosition = 3
                lastPositionSet = 1
            elif lastPositionSet == 0:
                lastPosition = 4
                lastPositionSet = 1

            if digitalOne == 1:
                if towerAxis > 0:
                    motorTwo = towerAxis
                else:
                    motorTwo = 0
            elif digitalTwo == 1:
                if towerAxis > 0:
                    motorTwo = towerAxis
                else:
                    motorTwo = 0
            else:
                motorTwo = towerAxis
        else:
            if digitalOne == 1:
                lastPosition = 0
                lastPositionSet = 1
            elif digitalTwo == 1:
                lastPosition = 4
                lastPositionSet = 1
            elif digitalThree == 1:
                lastPosition = 1
                lastPositionSet = 1
            elif digitalFour == 1:
                lastPosition = 2
                lastPositionSet = 1
            elif digitalFive == 1:
                lastPosition = 3
                lastPositionSet = 1
            elif lastPositionSet == 0:
                lastPosition = 4
                lastPositionSet = 1

            if targetPosition == 1:
                if digitalOne == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 0:
                    motorTwo = -1*TOWER_SPEED
                elif lastPosition < 0:
                    motorTwo = TOWER_SPEED
            if targetPosition == 2:
                if digitalThree == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 1:
                    motorTwo = -1*TOWER_SPEED
                elif lastPosition < 1:
                    motorTwo = TOWER_SPEED
            if targetPosition == 3:
                if digitalFour == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 2:
                    motorTwo = -1*TOWER_SPEED
                elif lastPosition < 2:
                    motorTwo = TOWER_SPEED
            if targetPosition == 4:
                if digitalFive == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 3:
                    motorTwo = -1*TOWER_SPEED
                elif lastPosition < 3:
                    motorTwo = TOWER_SPEED
            if targetPosition == 5:
                if digitalTwo == 1:
                    motorTwo = 0
                    targetPosition = 0
                elif lastPosition > 4:
                    motorTwo = -1*TOWER_SPEED
                elif lastPosition < 4:
                    motorTwo = TOWER_SPEED
                else:
                    motorTwo = TOWER_SPEED

    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, lastPosition, lastPositionSet, targetPosition, autoID, direction, speedMultiplier, autoStage
function [leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, lastPosition, lastPositionSet, targetPosition, autoID, direction, speedMultiplier, autoStage] = robot(leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, digitalSix, digitalSeven, digitalEight, digitalNine, driveFwd, driveSide, dbgUp, dbgDown, previousDbgDown, previousDbgUp, grip, release, previousGrip, previousRelease, towerAxis, lastPosition, lastPositionSet, turretAxis, analogOne, wristDown, wristUp, previousWristDown, previousWristUp, turretUp, previousTurretUp, previousTurretDown, turretDown, modeToggle, previousModeToggle, state, targetPosition, autoAButton, previousAutoAButton, autoBButton, previousAutoBButton, autoID, reverseButton, previousReverseButton, speedButton, previousSpeedButton, speedMultiplier, direction, autoStage)

    % Constants
    DRAWBRIDGE_OPEN = 127;
    DRAWBRIDGE_CLOSE = -127;
    DRIVETRAIN_SLOW_SPEED = 0.25;
    DRIVETRAIN_FAST_SPEED = 1;
    GRIPPER_OPEN = 127;
    GRIPPER_CLOSE = -127;
    TOWER_SPEED = 100;
    TURRET_UPPER_LIMIT = 100;
    TURRET_LOWER_LIMIT = -100;
    TURRET_SLOW_ROTATE_SPEED = 40;
    TURRET_FAST_ROTATE_SPEED = 100;
    TURRET_DEAD_ZONE = 5;
    TURRET_SLOW_ZONE = 10;
    TURRET_ANGLE_CONVERSION = 1;
    WRIST_ROTATE_INCREMENT = 10;
    AUTO_TOWER_START = 0;
    AUTO_TURRET_START_A = 0;
    AUTO_TURRET_START_B = 0;
    AUTO_GRIPPER_OPEN = 0;
    AUTO_WRIST_START = 0;
    AUTO_TURRET_ROTATION = 0;
    AUTO_BACK_SPEED = 0;
    AUTO_WRIST_END = 0;
    AUTO_TOWER_MIDDLE = 0;
    AUTO_GRIPPER_CLOSE = 0;
    AUTO_TOWER_END = 0;
    AUTO_FWD_SPEED = 0;

    % Button states
    if digitalEight == 1
        allowedStates = 1;
    else
        allowedStates = 0;
    end

    if autoAButton == 1 && previousAutoAButton == 0
        autoID = 1;
    elseif autoBButton == 1 && previousAutoBButton == 0
        autoID = 2;
    end

    if allowedStates == 1
        if modeToggle == 0 && previousModeToggle == 1
            if state == 1
                state = 2;
                autoStage = 1;
            elseif state == 2
                state = 1;
            end
        end
    elseif allowedStates == 0
        state = 0;
    end

    if state == 0
        left = driveFwd + driveSide;
        right = driveFwd - driveSide;

        if previousReverseButton == 1 && reverseButton == 0
            if direction == 0
                direction = 1;
            else
                direction = 0;
            end
        end

        if previousSpeedButton == 1 && speedButton == 0
            if speedMultiplier == DRIVETRAIN_FAST_SPEED
                speedMultiplier = DRIVETRAIN_SLOW_SPEED;
            else
                speedMultiplier = DRIVETRAIN_FAST_SPEED;
            end
        end

        left = left * speedMultiplier;
        right = right * speedMultiplier;

        if direction == 1
            left = -left;
            right = -right;
        end

        % 1 is backwards, 0 is forwards
        leftMotor = left;
        rightMotor = right;

        if dbgUp == 1 && previousDbgUp == 0
            servoThree = DRAWBRIDGE_OPEN;
        elseif dbgDown == 1 && previousDbgDown == 0
            servoThree = DRAWBRIDGE_CLOSE;
        end

        if release == 1 && previousRelease == 0
            servoOne = GRIPPER_OPEN;
        elseif grip == 1 && previousGrip == 0
            servoOne = GRIPPER_CLOSE;
        end

        if digitalOne == 1
            lastPosition = 0;
            lastPositionSet = 1;
        elseif digitalTwo == 1
            lastPosition = 4;
            lastPositionSet = 1;
        elseif digitalThree == 1
            lastPosition = 1;
            lastPositionSet = 1;
        elseif digitalFour == 1
            lastPosition = 2;
            lastPositionSet = 1;
        elseif digitalFive == 1
            lastPosition = 3;
            lastPositionSet = 1;
        elseif lastPositionSet == 0
            lastPosition = 4;
            lastPositionSet = 1;
        end

        if digitalOne == 1
            if towerAxis > 0
                motorTwo = towerAxis;
            else
                motorTwo = 0;
            end
        elseif digitalTwo == 1
            if towerAxis > 0
                motorTwo = towerAxis;
            else
                motorTwo = 0;
            end
        else
            motorTwo = towerAxis;
        end

        if analogOne > TURRET_UPPER_LIMIT
            if turretAxis < 0
                motorOne = turretAxis;
            else
                motorOne = 0;
            end
        elseif analogOne < TURRET_LOWER_LIMIT
            if turretAxis > 0
                motorOne = turretAxis;
            else
                motorOne = 0;
            end
        else
            motorOne = turretAxis;
        end

        if wristUp == 1 && previousWristUp == 1
            servoTwo = servoTwo + WRIST_ROTATE_INCREMENT;
        elseif wristDown == 1 && previousWristDown == 1
            servoTwo = servoTwo - WRIST_ROTATE_INCREMENT;
        end
    elseif state == 1
        if autoStage == 1
            if digitalOne == 1
                lastPosition = 0;
                lastPositionSet = 1;
            elseif digitalTwo == 1
                lastPosition = 4;
                lastPositionSet = 1;
            elseif digitalThree == 1
                lastPosition = 1;
                lastPositionSet = 1;
            elseif digitalFour == 1
                lastPosition = 2;
                lastPositionSet = 1;
            elseif digitalFive == 1
                lastPosition = 3;
                lastPositionSet = 1;
            elseif lastPositionSet == 0
                lastPosition = 4;
                lastPositionSet = 1;
            end

            if AUTO_TOWER_START == 1
                if digitalOne == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 0
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 0
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_START == 2
                if digitalThree == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 1
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 1
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_START == 3
                if digitalFour == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 2
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 2
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_START == 4
                if digitalFive == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 3
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 3
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_START == 5
                if digitalTwo == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 4
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 4
                    motorTwo = TOWER_SPEED;
                else
                    motorTwo = TOWER_SPEED;
                end
            end

            if autoID == 1
                AUTO_TURRET_START_A = AUTO_TURRET_START_A * TURRET_ANGLE_CONVERSION;
                if analogOne + TURRET_SLOW_ZONE > AUTO_TURRET_START_A
                    motorOne = TURRET_FAST_ROTATE_SPEED;
                elseif analogOne - TURRET_SLOW_ZONE < AUTO_TURRET_START_A
                    motorOne = -1 * TURRET_FAST_ROTATE_SPEED;
                elseif analogOne + TURRET_DEAD_ZONE > AUTO_TURRET_START_A
                    motorOne = TURRET_SLOW_ROTATE_SPEED;
                elseif analogOne - TURRET_DEAD_ZONE < AUTO_TURRET_START_A
                    motorOne = -1 * TURRET_SLOW_ROTATE_SPEED;
                else
                    motorOne = 0;
                end
            elseif autoID == 2
                AUTO_TURRET_START_B = AUTO_TURRET_START_B * TURRET_ANGLE_CONVERSION;
                if analogOne + TURRET_SLOW_ZONE > AUTO_TURRET_START_B
                    motorOne = TURRET_FAST_ROTATE_SPEED;
                elseif analogOne - TURRET_SLOW_ZONE < AUTO_TURRET_START_B
                    motorOne = -1 * TURRET_FAST_ROTATE_SPEED;
                elseif analogOne + TURRET_DEAD_ZONE > AUTO_TURRET_START_B
                    motorOne = TURRET_SLOW_ROTATE_SPEED;
                elseif analogOne - TURRET_DEAD_ZONE < AUTO_TURRET_START_B
                    motorOne = -1 * TURRET_SLOW_ROTATE_SPEED;
                else
                    motorOne = 0;
                end
            end

            servoOne = AUTO_GRIPPER_OPEN;
            servoTwo = AUTO_WRIST_START;

            if analogOne == AUTO_TURRET_ROTATION && digitalFour == 1
                autoStage = 2;
            end

        elseif autoStage == 2
            leftMotor = AUTO_BACK_SPEED;
            rightMotor = AUTO_BACK_SPEED;
            if digitalSix == 1 && digitalSeven == 1
                leftMotor = 0;
                rightMotor = 0;
                autoStage = 3;
            end

        elseif autoStage == 3
            servoTwo = AUTO_WRIST_END;
            autoStage = 4;

        elseif autoStage == 4
            % Repeat of last position setting
            if digitalOne == 1
                lastPosition = 0;
                lastPositionSet = 1;
            elseif digitalTwo == 1
                lastPosition = 4;
                lastPositionSet = 1;
            elseif digitalThree == 1
                lastPosition = 1;
                lastPositionSet = 1;
            elseif digitalFour == 1
                lastPosition = 2;
                lastPositionSet = 1;
            elseif digitalFive == 1
                lastPosition = 3;
                lastPositionSet = 1;
            elseif lastPositionSet == 0
                lastPosition = 4;
                lastPositionSet = 1;
            end

            if AUTO_TOWER_MIDDLE == 1
                if digitalOne == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 0
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 0
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_MIDDLE == 2
                if digitalThree == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 1
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 1
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_MIDDLE == 3
                if digitalFour == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 2
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 2
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_MIDDLE == 4
                if digitalFive == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 3
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 3
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_MIDDLE == 5
                if digitalTwo == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 4
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 4
                    motorTwo = TOWER_SPEED;
                else
                    motorTwo = TOWER_SPEED;
                end
            end

            if digitalThree == 1
                autoStage = 5;
            end

        elseif autoStage == 5
            servoOne = AUTO_GRIPPER_CLOSE;
            autoStage = 6;

        elseif autoStage == 6
            % Repeat of last position setting
            if digitalOne == 1
                lastPosition = 0;
                lastPositionSet = 1;
            elseif digitalTwo == 1
                lastPosition = 4;
                lastPositionSet = 1;
            elseif digitalThree == 1
                lastPosition = 1;
                lastPositionSet = 1;
            elseif digitalFour == 1
                lastPosition = 2;
                lastPositionSet = 1;
            elseif digitalFive == 1
                lastPosition = 3;
                lastPositionSet = 1;
            elseif lastPositionSet == 0
                lastPosition = 4;
                lastPositionSet = 1;
            end

            if AUTO_TOWER_END == 1
                if digitalOne == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 0
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 0
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_END == 2
                if digitalThree == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 1
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 1
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_END == 3
                if digitalFour == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 2
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 2
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_END == 4
                if digitalFive == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 3
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 3
                    motorTwo = TOWER_SPEED;
                end
            elseif AUTO_TOWER_END == 5
                if digitalTwo == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 4
                    motorTwo = -1 * TOWER_SPEED;
                elseif lastPosition < 4
                    motorTwo = TOWER_SPEED;
                else
                    motorTwo = TOWER_SPEED;
                end
            end
        end
    elseif state == 2

        % Drive calculations
        left = driveFwd + driveSide;
        right = driveFwd - driveSide;

        % Reverse direction toggle
        if previousReverseButton == 1 && reverseButton == 0
            if direction == 0
                direction = 1;
            else
                direction = 0;
            end
        end

        % Speed multiplier toggle
        if previousSpeedButton == 1 && speedButton == 0
            if speedMultiplier == 1
                speedMultiplier = 0.25;
            else
                speedMultiplier = 1;
            end
        end

        % Apply speed multiplier
        left = left * speedMultiplier;
        right = right * speedMultiplier;

        % Reverse direction if applicable
        if direction == 1
            left = -left;
            right = -right;
        end

        % Set motor speeds
        leftMotor = left;
        rightMotor = right;

        % Servo control for drawbridge
        if dbgUp == 1 && previousDbgUp == 0
            servoThree = DRAWBRIDGE_OPEN;
        elseif dbgDown == 1 && previousDbgDown == 0
            servoThree = DRAWBRIDGE_CLOSE;
        end

        % Gripper control
        if release == 1 && previousRelease == 0
            servoOne = GRIPPER_OPEN;
        elseif grip == 1 && previousGrip == 0
            servoOne = GRIPPER_CLOSE;
        end

        % Turret movement logic
        if analogOne > TURRET_UPPER_LIMIT
            if turretAxis < 0
                motorOne = turretAxis;
            else
                motorOne = 0;
            end
        elseif analogOne < TURRET_LOWER_LIMIT
            if turretAxis > 0
                motorOne = turretAxis;
            else
                motorOne = 0;
            end
        else
            motorOne = turretAxis;
        end

        % Wrist control
        if wristUp == 1 && previousWristUp == 1
            servoTwo = servoTwo + WRIST_ROTATE_INCREMENT;
        elseif wristDown == 1 && previousWristDown == 1
            servoTwo = servoTwo - WRIST_ROTATE_INCREMENT;
        end

        % Turret position adjustment
        if turretUp == 1 && previousTurretUp == 1
            targetPosition = lastPosition + 1;
        elseif turretDown == 1 && previousTurretDown == 1
            targetPosition = lastPosition - 1;
        end

        % Tower movement based on target position
        if targetPosition == 0
            % Tower stops when in position 0
            if digitalOne == 1
                lastPosition = 0;
                lastPositionSet = 1;
            elseif digitalTwo == 1
                lastPosition = 4;
                lastPositionSet = 1;
            elseif digitalThree == 1
                lastPosition = 1;
                lastPositionSet = 1;
            elseif digitalFour == 1
                lastPosition = 2;
                lastPositionSet = 1;
            elseif digitalFive == 1
                lastPosition = 3;
                lastPositionSet = 1;
            elseif lastPositionSet == 0
                lastPosition = 4;
                lastPositionSet = 1;
            end

            % Tower motor control based on axis
            if digitalOne == 1 || digitalTwo == 1
                if towerAxis > 0
                    motorTwo = towerAxis;
                else
                    motorTwo = 0;
                end
            else
                motorTwo = towerAxis;
            end
        else
            % Set last position based on target position
            if digitalOne == 1
                lastPosition = 0;
                lastPositionSet = 1;
            elseif digitalTwo == 1
                lastPosition = 4;
                lastPositionSet = 1;
            elseif digitalThree == 1
                lastPosition = 1;
                lastPositionSet = 1;
            elseif digitalFour == 1
                lastPosition = 2;
                lastPositionSet = 1;
            elseif digitalFive == 1
                lastPosition = 3;
                lastPositionSet = 1;
            elseif lastPositionSet == 0
                lastPosition = 4;
                lastPositionSet = 1;
            end

            % Motor movement logic for tower based on target position
            if targetPosition == 1
                if digitalOne == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 0
                    motorTwo = -TOWER_SPEED;
                elseif lastPosition < 0
                    motorTwo = TOWER_SPEED;
                end
            elseif targetPosition == 2
                if digitalThree == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 1
                    motorTwo = -TOWER_SPEED;
                elseif lastPosition < 1
                    motorTwo = TOWER_SPEED;
                end
            elseif targetPosition == 3
                if digitalFour == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 2
                    motorTwo = -TOWER_SPEED;
                elseif lastPosition < 2
                    motorTwo = TOWER_SPEED;
                end
            elseif targetPosition == 4
                if digitalFive == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 3
                    motorTwo = -TOWER_SPEED;
                elseif lastPosition < 3
                    motorTwo = TOWER_SPEED;
                end
            elseif targetPosition == 5
                if digitalTwo == 1
                    motorTwo = 0;
                    targetPosition = 0;
                elseif lastPosition > 4
                    motorTwo = -TOWER_SPEED;
                elseif lastPosition < 4
                    motorTwo = TOWER_SPEED;
                else
                    motorTwo = TOWER_SPEED;
                end
            end
        end
    end





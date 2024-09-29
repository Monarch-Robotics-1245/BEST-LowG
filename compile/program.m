function [leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier, lastPosition, lastPositionSet] = robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, analogOne, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, lastPosition, lastPositionSet, previousSevenU, previousSevenL, previousEightR, previousEightL, leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier)
    left = axisOne + axisTwo;
    right = axisOne - axisTwo;

    if previousEightR == 1 && eightR == 0
        if direction == 0
            direction = 1;
        else
            direction = 0;
        end
    end

    if previousEightL == 1 && eightL == 0
        if speedMultiplier == 1
            speedMultiplier = 0.25;
        else
            speedMultiplier = 1;
        end
    end

    left = left * speedMultiplier;
    right = right * speedMultiplier;

    if direction == 1
        left = -left;
        right = -right;
    end

    leftMotor = left;
    rightMotor = right;

    if sevenU == 1 && previousSevenU == 0
        servoThree = 127;
    elseif sevenL == 1 && previousSevenL == 0
        servoThree = -127;
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
        if axisFour > 0
            motorTwo = axisFour;
        else
            motorTwo = 0;
        end
    elseif digitalTwo == 1
        if axisFour > 0
            motorTwo = axisFour;
        else
            motorTwo = 0;
        end
    else
        motorTwo = axisFour;
    end

    if analogOne > 100
        if 0 > axisThree
            motorOne = axisThree;
        else
            motorOne = 0;
        end
    elseif analogOne < -100
        if 0 < axisThree
            motorOne = axisThree;
        else
            motorOne = 0;
        end
    else
        motorOne = axisThree;
    end

    if fiveU == 1 && fiveD == 1
        % do nothing
    elseif fiveU == 1
        servoTwo = servoTwo + 10;
    elseif fiveD == 1
        servoTwo = servoTwo - 10;
    end

    direction = direction;
    speedMultiplier = speedMultiplier;

end
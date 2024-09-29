def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, analogOne, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, lastPosition, lastPositionSet, previousSevenU, previousSevenL, previousEightR, previousEightL, leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier):
    left = axisOne + axisTwo
    right = axisOne - axisTwo
    if previousEightR == 1 and eightR == 0:
        if direction == 0:
            direction = 1
        else:
            direction = 0
    if previousEightL == 1 and eightL == 0:
        if speedMultiplier == 1:
            speedMultiplier = .25
        else:
            speedMultiplier = 1
    left = left * speedMultiplier
    right = right * speedMultiplier
    if direction == 1:
        left = -left
        right = -right
    leftMotor = left
    rightMotor = right
    if sevenU == 1 & previousSevenU == 0:
        servoThree = 127
    elif sevenL == 1 & previousSevenL == 0:
        servoThree = -127
    if sevenU == 1 & previousSevenU == 0:
        servoThree = 127
    elif sevenL == 1 & previousSevenL == 0:
        servoThree = -127
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
        if axisFour > 0:
            motorTwo = axisFour
        else:
            motorTwo = 0
    elif digitalTwo == 1:
        if axisFour > 0:
            motorTwo = axisFour
        else:
            motorTwo = 0
    else:
        motorTwo = axisFour
    if analogOne > 100:
        if 0 > axisThree:
            motorOne = axisThree
        else:
            motorOne = 0
    elif analogOne < -100:
        if 0 < axisThree:
            motorOne = axisThree
        else:
            motorOne = 0
    else:
        motorOne = axisThree
    if fiveU == 1 & fiveD == 1:
        pass
    elif fiveU == 1:
        servoTwo += 10
    elif fiveD == 1:
        servoTwo -= 10
    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour, direction, speedMultiplier, lastPosition, lastPositionSet
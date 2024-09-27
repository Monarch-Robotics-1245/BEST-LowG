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

import constants.tower

def setTowerMotor(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, motorTwo, value, lastPosition, lastPositionSet):
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
        if value > 0:
            motorTwo = value
        else:
            motorTwo = 0
    elif digitalTwo == 1:
        if value > 0:
            motorTwo = value
        else:
            motorTwo = 0
    else:
        motorTwo = value

def setTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, motorTwo, position, lastPosition, lastPositionSet):
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

    if position == 0:
        if digitalOne == 1:
            motorTwo = 0
        elif lastPosition > 0:
            motorTwo = -constants.tower.TOWER_SPEED
        elif lastPosition < 0:
            motorTwo = constants.tower.TOWER_SPEED
    if position == 1:
        if digitalThree == 1:
            motorTwo = 0
        elif lastPosition > 1:
            motorTwo = -constants.tower.TOWER_SPEED
        elif lastPosition < 1:
            motorTwo = constants.tower.TOWER_SPEED
    if position == 2:
        if digitalFour == 1:
            motorTwo = 0
        elif lastPosition > 2:
            motorTwo = -constants.tower.TOWER_SPEED
        elif lastPosition < 2:
            motorTwo = constants.tower.TOWER_SPEED
    if position == 3:
        if digitalFive == 1:
            motorTwo = 0
        elif lastPosition > 3:
            motorTwo = -constants.tower.TOWER_SPEED
        elif lastPosition < 3:
            motorTwo = constants.tower.TOWER_SPEED
    if position == 4:
        if digitalTwo == 1:
            motorTwo = 0
        elif lastPosition > 4:
            motorTwo = -constants.tower.TOWER_SPEED
        elif lastPosition < 4:
            motorTwo = constants.tower.TOWER_SPEED
        else:
            motorTwo = constants.tower.TOWER_SPEED


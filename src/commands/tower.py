"""
This is the tower command.
"""
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

import src.subsystems.tower


def moveTower(towerAxis, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, lastPosition, lastPositionSet):
    """
    lastPositionSet (int): Updates last position the tower was at
    lastPosition (int): Takes in last position the tower was at
    digitalFive (int): Takes in IR sensor values
    digitalFour (int): Takes in IR sensor values
    digitalThree (int): Takes in IR sensor values
    digitalTwo (int): Takes in limit switch values

    digitalOne (int): Takes in limit switch values
    Takes in joystick values and sets the parameters for the subsystem file's function.
    """
    src.subsystems.tower.setTowerMotor(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, towerAxis, lastPosition, lastPositionSet)

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

import subsystems.tower


def moveTower(motorTwo, axisFour, digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, lastPosition,
              lastPositionSet):
    """
    Takes in joystick values and sets the parameters for the subsystem file's function.

    digitalOne (int): Takes in limit switch values
    digitalTwo (int): Takes in limit switch values
    digitalThree (int): Takes in IR sensor values
    digitalFour (int): Takes in IR sensor values
    digitalFive (int): Takes in IR sensor values
    lastPosition (int): Takes in last position the tower was at
    lastPositionSet (int): Updates last position the tower was at
    """
    subsystems.tower.setTowerMotor(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, motorTwo, axisFour,
                                   lastPosition, lastPositionSet)

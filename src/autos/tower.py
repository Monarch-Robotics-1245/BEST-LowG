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

import src.constants.tower
import src.subsystems.tower


def autoTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, motorTwo, lastPosition, lastPositionSet):
    src.subsystems.tower.setTowerPosition(digitalOne, digitalTwo, digitalThree, digitalFour, digitalFive, motorTwo, src.constants.tower.TOWER_AUTO_POSITION, lastPosition, lastPositionSet)

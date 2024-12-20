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

import src.constants.wrist

servoTwo = 0

def wristUp():
    global servoTwo
    servoTwo += src.constants.wrist.ROTATE_INCREMENT


def wristDown():
    global servoTwo
    servoTwo -= src.constants.wrist.ROTATE_INCREMENT


def setWrist(value):
    global servoTwo
    servoTwo = value

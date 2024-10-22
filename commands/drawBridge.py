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

import subsystems.drawBridge


def runDrawBridge(dbgUp, dbgDown, previousDbgUp, previousDbgDown):
    if dbgUp == 1 and previousDbgUp == 0:
        subsystems.drawBridge.openDrawBridge()

    Takes in the joystick values and sets the DrawBridge servo to those values.
    """
    elif dbgDown == 1 and previousDbgDown == 0:
        subsystems.drawBridge.closeDrawBridge()

    servoThree (int): Takes in values 127 and -127 for up and down
    sixU (int): Joystick Button 6 Up
    sixD (int): Joystick Button 6 Down
    previousSixU (int): Joystick Button 6 up previous
    previousSixD (int): Joystick Button 6 down previous
    """
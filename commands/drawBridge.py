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
    """
    Takes in the joystick values and sets the DrawBridge servo to those values.

    dbgUp (int): Drawbridge Button Up
    dbgDown (int): Drawbridge Button Down
    previousDbgUp (int): Drawbridge Button up previous
    previousDbgDown (int): Drawbridge Button down previous
    """
    if dbgUp == 1 and previousDbgUp == 0:
        subsystems.drawBridge.openDrawBridge()

    elif dbgDown == 1 and previousDbgDown == 0:
        subsystems.drawBridge.closeDrawBridge()

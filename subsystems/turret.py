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
# AnalogOne

import constants.turret

def setTurretMotor(analogOne, motorOne, value):
    if analogOne > constants.turret.TURRET_UPPER_LIMIT:
        if 0 > value:
            motorOne = value
        else:
            motorOne = 0
    elif analogOne < constants.turret.TURRET_LOWER_LIMIT:
        if 0 < value:
            motorOne = value
        else:
            motorOne = 0
    else:
        motorOne = value

def setTurretRotation(analogOne, motorOne, rotation):
    rotation *= constants.turret.TURRET_ANGLE_CONVERSION
    if analogOne + constants.turret.TURRET_SLOW_ZONE > rotation:
        motorOne = constants.turret.TURRET_FAST_ROTATE_SPEED
    elif analogOne - constants.turret.TURRET_SLOW_ZONE < rotation:
        motorOne = -constants.turret.TURRET_FAST_ROTATE_SPEED
    elif analogOne + constants.turret.TURRET_DEAD_ZONE > rotation:
        motorOne = constants.turret.TURRET_SLOW_ROTATE_SPEED
    elif analogOne - constants.turret.TURRET_DEAD_ZONE < rotation:
        motorOne = -constants.turret.TURRET_SLOW_ROTATE_SPEED
    else:
        motorOne = 0



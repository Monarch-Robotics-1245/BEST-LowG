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

import src.subsystems.gripper

def gripper(grip, release, previousGrip, previousRelease):
    """
    Takes in the joystick values and sets the gripper servo to those values

    servoOne (int): Takes in values 127 and -127 for setting gripper to close and open positions.
    sevenU (int): Joystick Button 7 up
    sevenL (int): Joystick Button 7 left
    previousSevenU (int): Joystick Button 7 up previous
    previousSevenL (int): Joystick Button 7 left previous
    """

    if release == 1 and previousRelease == 0:
        src.subsystems.gripper.openGripper()
    elif grip == 1 and previousGrip == 0:
        src.subsystems.gripper.closeGripper()


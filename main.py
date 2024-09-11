import subsystems.drivetrain
import autos.auto
import subsystems.servo


def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, previousServoOne):

    leftMotor = 0
    rightMotor = 0
    motorOne = 0
    motorTwo = 0
    servoOne = 0
    servoTwo = 0
    servoThree = 0
    servoFour = 0

    subsystems.drivetrain.drive(axisTwo, axisThree)
    autos.auto.auto()
    subsystem.servo.servo(sevenU, sevenL, previousServoOne)
    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour

import subsystems.drivetrain
import autos.auto
import subsystems.servo


def robot(axisOne, axisTwo, axisThree, axisFour, fiveU, fiveD, sixU, sixD, sevenU, sevenL, sevenR, sevenD, eightR, eightD, eightU, eightL, priviousServoOne):

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
    subsystems.servo.servo(sevenU,sevenL,priviousServoOne)
    return leftMotor, rightMotor, motorOne, motorTwo, servoOne, servoTwo, servoThree, servoFour

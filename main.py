# VEX EDR Python-Project
import vex
import constants.constants as constants

# region config
joystick = vex.Joystick()
leftMotor = vex.Motor(constants.LEFT_MOTOR_ID, constants.LEFT_MOTOR_POLARITY)
rightMotor = vex.Motor(constants.RIGHT_MOTOR_ID, constants.RIGHT_MOTOR_POLARITY)
# endregion config

leftMotor.run(joystick.axis3())
rightMotor.run(joystick.axis2())


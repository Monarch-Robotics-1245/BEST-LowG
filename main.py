# VEX EDR Python-Project
import vex
import constants.constants as constants
import autos.auto as auto

# region config
joystick = vex.Joystick()
leftMotor = vex.Motor(constants.LEFT_MOTOR_ID, constants.LEFT_MOTOR_POLARITY)
rightMotor = vex.Motor(constants.RIGHT_MOTOR_ID, constants.RIGHT_MOTOR_POLARITY)
# endregion config

while True:
    if joystick.b7left():
        auto.runAuto()

    # drivetrain.runDrivetrain()

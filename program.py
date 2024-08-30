# Merging constants/py
from unittest.mock import right

LEFT_MOTOR_ID = 1
RIGHT_MOTOR_ID = 2
RIGHT_MOTOR_POLARITY = False
LEFT_MOTOR_POLARITY = True
# Merging main.py
# VEX EDR Python-Project
import sys
import vex

#region config
joystick = vex.Joystick()
leftMotor = vex.Motor(LEFT_MOTOR_ID, LEFT_MOTOR_POLARITY)
rightMotor = vex.Motor(RIGHT_MOTOR_ID, RIGHT_MOTOR_POLARITY)
#endregion config

joystick.debug_set_axis2(50)
joystick.debug_set_axis3(75)

joystick.debug_print_values()

leftMotorSpeed = joystick.axis2()
rightMotorSpeed = joystick.axis3()

leftMotor.run(leftMotorSpeed)
rightMotor.run(rightMotorSpeed)


leftMotor.debug_print_value()
rightMotor.debug_print_value()
rightMotor.debug_print_switch_polarity()
leftMotor.debug_print_switch_polarity()
###########################################################################
#                                                                         #
#                            VEX Lib for Python                           #
#                            Filename: vexLib.py                          #
#                                Version: 1                               #
#                         Author: Matthew Spratlin                        #
#                                                                         #
#                          ©2024 Matthew Spratlin                         #
#                                                                         #
#                    PROPRIETARY SOFTWARE DO NOT SHARE                    #
#                                                                         #
#          THE UNAUTHORIZED USE, COPYING, MODIFICATION, MERGING,          #
#          PUBLISHING, DISTRIBUTION, SUBLICENSING, OR SELLING OF          #
#          COPIES OF THE SOFTWARE, AS WELL AS ANY FACILITATION            #
#              THEREOF, AND PERMITTING OTHERS TO DO SO, ARE               #
#                   STRICTLY PROHIBITED WITHOUT PRIOR                     #
#                        EXPLICIT WRITTEN CONSENT.                        #
#                                                                         #
#             THE ABOVE COPYRIGHT NOTICE AND THIS PERMISSION              #
#          NOTICE SHALL BE INCLUDED IN ALL COPIES OR SUBSTANTIAL          #
#                        PORTIONS OF THE SOFTWARE.                        #
#                                                                         #
#           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY            #
#           OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT            #
#          LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS          #
#           FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO           #
#             EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE             #
#            LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,            #
#                WHETHER IN AN ACTION OF CONTRACT, TORT OR                #
#            OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION             #
#            WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN            #
#                              THE SOFTWARE.                              #
#                                                                         #
###########################################################################

UNIT_INCH = 1
"""Identifier for Inches"""
UNIT_CM = 2
"""Identifier for Centimeters"""
UNIT_MM = 3
"""Identifier for Millimeters"""

analogMaxValue = 100
"""Max Analog Input Value"""
analogMinValue = 0
"""Min Analog Input Value"""


class DigitalInput:
    """Digital Inputs (Sensors)"""
    def __init__(self, pin):
        """Initialize with the digital Pin"""
        self.pin = pin
        """Pin number of sensor (Private)"""
        self.state = False
        """Sensors current state (Private)"""
    def debug_set_state(self, state):
        self.state = state

    def debug_print_state(self):
        print(self.state)

    def is_on(self):
        return self.state


class DigitalOutput:
    def __init__(self, pin):
        self.pin = pin
        self.state = False

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def is_on(self):
        return self.state

    def debug_print_state(self):
        print(self.state)


class AnalogSensor:
    def __init__(self, pin):
        self.pin = pin
        self.value = 0

    def debug_set_value(self, value):
        self.value = value

    def raw_value(self):
        return self.value

    def percent(self):
        return self.value / analogMaxValue * 100

    def debug_print_value(self):
        print(self.value)


class Motor:
    def __init__(self, pin, switch_polarity):
        self.pin = pin
        self.value = 0
        self.switch_polarity = switch_polarity

    def off(self):
        self.value = 0

    def run(self, value):
        self.value = value/100*127

    def raw_run(self, value):
        self.value = value

    def debug_print_value(self):
        print(self.value)

    def debug_print_switch_polarity(self):
        print(self.switch_polarity)


class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.value = 0

    def position(self, position):
        self.value = position

    def debug_print_value(self):
        print(self.value)


class Joystick:
    def __init__(self, is_partner=False):
        self.is_partner = is_partner
        self.axis1 = 0
        self.axis2 = 0
        self.axis3 = 0
        self.axis4 = 0
        self.accelX = 0
        self.accelY = 0
        self.b5up = False
        self.b5down = False
        self.b6up = False
        self.b6down = False
        self.b7up = False
        self.b7down = False
        self.b7left = False
        self.b7right = False
        self.b8up = False
        self.b8down = False
        self.b8left = False
        self.b8right = False
        self.deadband = 0

    def is_partner(self):
        return self.is_partner

    def set_deadband(self, deadband):
        self.deadband = deadband

    def axis1(self):
        return self.axis1

    def axis2(self):
        return self.axis2

    def axis3(self):
        return self.axis3

    def axis4(self):
        return self.axis4

    def accelX(self):
        return self.accelX

    def accelY(self):
        return self.accelY

    def b5up(self):
        return self.b5up

    def b5down(self):
        return self.b5down

    def b6up(self):
        return self.b6up

    def b6down(self):
        return self.b6down

    def b7up(self):
        return self.b7up

    def b7down(self):
        return self.b7down

    def b7left(self):
        return self.b7left

    def b7right(self):
        return self.b7right

    def b8up(self):
        return self.b8up

    def b8down(self):
        return self.b8down

    def b8left(self):
        return self.b8left

    def b8right(self):
        return self.b8right

    def debug_print_values(self):
        print(self.axis1)
        print(self.axis2)
        print(self.axis3)
        print(self.axis4)
        print(self.accelX)
        print(self.accelY)
        print(self.b5up)
        print(self.b5down)
        print(self.b6up)
        print(self.b6down)
        print(self.b7up)
        print(self.b7down)
        print(self.b7left)
        print(self.b7right)
        print(self.b8up)
        print(self.b8down)
        print(self.b8left)
        print(self.b8right)
        print(self.deadband)
        print(self.is_partner)

    def debug_set_axis1(self, value):
        self.axis1 = value

    def debug_set_axis2(self, value):
        self.axis2 = value

    def debug_set_axis3(self, value):
        self.axis3 = value

    def debug_set_axis4(self, value):
        self.axis4 = value

    def debug_set_accelX(self, value):
        self.accelX = value

    def debug_set_accelY(self, value):
        self.accelY = value

    def debug_set_b5up(self, value):
        self.b5up = value

    def debug_set_b5down(self, value):
        self.b5down = value

    def debug_set_b6up(self, value):
        self.b6up = value

    def debug_set_b6down(self, value):
        self.b6down = value

    def debug_set_b7up(self, value):
        self.b7up = value

    def debug_set_b7down(self, value):
        self.b7down = value

    def debug_set_b7left(self, value):
        self.b7left = value

    def debug_set_b7right(self, value):
        self.b7right = value

    def debug_set_b8up(self, value):
        self.b8up = value

    def debug_set_b8down(self, value):
        self.b8down = value

    def debug_set_b8left(self, value):
        self.b8left = value

    def debug_set_b8right(self, value):
        self.b8right = value

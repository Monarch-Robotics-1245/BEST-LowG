//new practice function
def servo(sevenU, sevenL, previousServoOne):
    if sevenU==1: //1=(pressed)
        servoOne=127
    elseif sevenL=1:
        servoOne=0
    else:
        servoOne=previousServoOne

    
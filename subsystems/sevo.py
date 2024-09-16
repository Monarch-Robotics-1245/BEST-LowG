def servo(sevenU, sevenL, priviousServoOne)
    if sevenU == 1
        servoOne = 127
    elif sevenL ==1
        servoOne = 0
    else
        servoOne = priviousServoOne
        
![Stars](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=stars&cacheSeconds=10)
![Forks](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=forks&cacheSeconds=10)
![Watchers](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=watchers&cacheSeconds=10)
![Commits](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=commits&cacheSeconds=10)
![Last Release](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=last-release&cacheSeconds=10)
![Last Release Date](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=last-release-date&cacheSeconds=10)
![Last Commit Date](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=last-commit&cacheSeconds=10)
![Pull Requests](https://img.shields.io/endpoint?url=https://monarchlowg-private-repo-badges-23423423.vercel.app/api/fetchRepoData?type=pull-requests&cacheSeconds=10)
![Qodana](https://github.com/Monarch-Robotics-1245/BEST-LowG/actions/workflows/qodana_code_quality.yml/badge.svg)(https://github.com/Monarch-Robotics-1245/BEST-LowG/actions/workflows/qodana_code_quality.yml)

# BEST LowG
## **Description**
Monarch Robotics code for the 2024 BEST LowG Season
## **Project Structure**
### `main.py`
The main file that runs the robot code. This file should be run on the robot.
Commands and autos can be run from this file.
### `commands/`
This directory contains all the commands that the robot can run. 
Commands are reusable pieces of code that can be run from the main file. 
Commands are used for manual actions done by the driver.
### `autos/`
This directory contains all the autonomous routines that the robot can run. 
Autos are reusable pieces of code that can be run from the main file. 
Autos are used for autonomous actions done by the robot. 
Autos are also used for driver assistance during the teleop period.
### `subsystems/`
This directory contains all the subsystems that the robot uses. 
Subsystems are reusable pieces of code that can be run from the main file. 
Subsystems are used for controlling the robot's hardware.
## **EyeSight**
EyeSight is the driver assistance technology system that the robot runs. 
It is toggleable by the driver and only runs when the onboard enable switch is inserted. 
EyeSight is used to assist the driver in the teleop period. EyeSight is not used in the autonomous period. 
EyeSight files are called by `main.py` and are located in the `autos/` directory.
## **Python Comment Syntax**
### Block Comment
A block comment explains a section of code and spans multiple lines. Each line starts with a `#` followed by a space. 
These comments describe *how* or *why* the code works, and should be used for larger code explanations.

```python
# This is a block comment explaining the following code.
# It helps to clarify complex logic or describe non-obvious code behavior.

for i in range(10):
    print(i)
```
> We mainly use block comments
### Docstring
A docstring is a string literal used to document modules, classes, and functions. It describes *what* the code does. 
Docstrings are enclosed in triple quotes (`"""`) and placed inside the function, class, or module definition.

```python
def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b
```

## **Ports and Inputs**
### Motors
```text
Port 1:  N/P
Port 2:  Left
Port 3:  Right
Port 4:  Tower
Port 5:  Turret
Port 6:  Gripper
Port 7:  Wrist
Port 8:  DBG1
Port 9:  DBG2
Port 10: N/P
```
> Motors should be set to a double from a range of -127 to 127 where 127 is 100% and -127 is -100%
### Digital Inputs
```text
Digital 1: 
```
> Digital Inputs output a 1 for True and a 0 for False. They are not boolean variables
### Analog Inputs
```text
Analog 1: 
```
> Analog Inputs output a range from -127 to 127 where 127 is 100% and -127 is -100%
### Joystick Controls
```text
Axis 1 (Right Horizontal):  
Axis 2 (Right Vertical):    
Axis 3 (Left Horizontal):   
Axis 4 (Left Vertical):     
5U (Left Up):               
5D (Left Down):             
6U (Right Up):              
6D (Right Down):            
7U (Left DPad Up):          
7L (Left DPad Left):        
7D (Left DPad Down):        
7R (Left DPad Right):       
8U (Right DPad Up):         
8L (Right DPad Left):       
8D (Right DPad Down):       
8R (Right DPad Right):      
```
> Joystick Buttons output a 1 for True and a 0 for False. They are not boolean variables

> Joystick Axis output a range from -127 to 127 where 127 is 100% and -127 is -100%
## **Code Formatting**
Please try to follow the PEP 8 Style Guide. 

Please insert this code snippet at the top of all files to initialize the function variables. 
This may be changed over the season:
```python
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
```

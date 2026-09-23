# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:58
# FILE: ex_24_draw_string.py
# AUTHOR: Randall Nagy
#

import turtle as robot

ref = robot.numinput('Press Cancel To Quit', "Rectangle Size?")
if ref is not None:
    color = robot.textinput('Press Cancel To Quit', "Rectangle Color?")
    if color is not None:
        robot.penup()
        robot.goto(-300, 200)
        font = ("Times", 24, "bold")
        robot.write("You entered: " + str(ref) +", " + color, font=font)

robot.done()


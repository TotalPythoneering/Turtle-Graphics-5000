# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_25_circles.py
# AUTHOR: Randall Nagy
#

import turtle as robot

robot.color('purple')
robot.fillcolor('gold')
robot.hideturtle()
robot.begin_fill()
robot.pensize(10)
robot.circle(100)
robot.end_fill()

robot.goto(100, -100)
robot.dot(50, "aqua")

robot.done()



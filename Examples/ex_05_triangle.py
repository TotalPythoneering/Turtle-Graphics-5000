# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_05_triangle.py
# AUTHOR: Randall Nagy
#

import turtle

sides = 3 # Triangle
zangle = 360 / sides
print("Sides #", sides, "angle is", zangle)
for side in range(sides):
    turtle.forward(100)
    turtle.right(zangle)

turtle.done()



# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_38_shape_properties.py
# AUTHOR: Randall Nagy
#

import turtle


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.begin_poly()
turtle.pensize("10")
turtle.color("blue")
for seg in range(10, 100, 5):
    turtle.left(45)
    turtle.forward(seg)
turtle.end_poly()

print(turtle.getscreen())
# Tkinter Canvas:
can = turtle.getscreen().getcanvas()
can.postscript(file = "turtle.eps")

turtle.done()


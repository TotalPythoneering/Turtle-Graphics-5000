# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_16_pen_updown.py
# AUTHOR: Randall Nagy
#

import turtle

# Draw a dashed line
even = True
for seg in range(10, 100, 5):
    if even:
        turtle.penup()
        even = False
    else:
        turtle.pendown()
        even = True
    turtle.forward(12)


turtle.done()


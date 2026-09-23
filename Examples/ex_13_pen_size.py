# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_13_pen_size.py
# AUTHOR: Randall Nagy
#

import turtle

pen = turtle.pen()
pen['pensize'] = 15
pen['pencolor'] = 'green'
turtle.pen(pen)
turtle.forward(100)

turtle.left(90)
turtle.pensize(turtle.pensize() * 2)
turtle.color('red')
turtle.forward(100)

turtle.left(90)
turtle.width(turtle.width()*2)
turtle.color('blue')
turtle.forward(100)

turtle.done()




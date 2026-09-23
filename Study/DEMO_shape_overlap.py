# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-06 04:29:14
# FILE: DEMO_shape_overlap.py
# AUTHOR: Randall Nagy
# DEMO_shape_overlap.py
#
import turtle

shape = "classic"
t1 = turtle.Turtle(shape);t1.color("red")
t2 = turtle.Turtle(shape);t2.color("blue")

t1.goto(40,0)

t1.shapesize(8, 8, 7)
t2.shapesize(18, 18, 7)

t1.onclick(lambda x, y: print("t1 click", x, y))
t2.onclick(lambda x, y: print("t2 click", x, y))


# turtle.listen()
turtle.done()



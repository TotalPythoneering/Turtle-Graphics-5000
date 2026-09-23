# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-20 07:41:32
# FILE: LAB_BigTurtle.py
# AUTHOR: Randall Nagy
# LAB_BigTurtle.py
#
import turtle


turtle.hideturtle()

# Shape & colors
turtle.shape('turtle')

# 10x
size = turtle.turtlesize();print(size)
turtle.turtlesize(size[0] * 10, size[1] * 10, 7)

# Read new size
size = turtle.turtlesize()
print(size)

# Requested colors
radius = size[0] * size[1] * 4
turtle.color("brown")
turtle.dot(radius, "green") # Note effective color!

# Depicted results
turtle.fillcolor('gold')
turtle.left(90)
turtle.showturtle()

turtle.done()

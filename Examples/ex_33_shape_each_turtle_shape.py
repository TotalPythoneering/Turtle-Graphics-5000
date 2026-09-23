# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_33_shape_each_turtle_shape.py
# AUTHOR: Randall Nagy
#

import turtle

# Common Display
def shape_draw(name, x_pos, y_pos):
    turtle.hideturtle()
    turtle.goto(x_pos, y_pos)
    turtle.shape(name)
    turtle.turtlesize(20, 20, 15)
    turtle.pendown()
    turtle.color('green')
    turtle.pensize(10)
    turtle.fillcolor('gold')
    turtle.showturtle()

# Pre-Defined Shapes
shapes = turtle.getshapes()

# Show Each Shape
for shape in shapes:
    turtle.penup()
    turtle.goto(0, 0)
    shape_draw(shape, 100, 0)
    turtle.textinput("Shape: " + shape, "Click to Continue")

turtle.done()


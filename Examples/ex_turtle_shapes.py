# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_turtle_shapes.py
# AUTHOR: Randall Nagy
# ex_turtle_shapes.py
#
import turtle


def jot(str):
    turtle.hideturtle()
    pos = turtle.pos() # save where we are
    turtle.goto(pos[0] - 20, pos[1] - 80)
    turtle.write(str)
    turtle.goto(pos[0], pos[1])
    turtle.showturtle()


# Pre-Defined Shapes
shapes = turtle.getshapes()

turtle.turtlesize(4, 4, 1)
turtle.color('green')
turtle.fillcolor('gold')
turtle.penup()
turtle.goto(-400, -60)
for shape in shapes:
    turtle.forward(100)
    turtle.shape(shape)
    id = turtle.stamp()
    jot(shape + " = " + str(id))

turtle.done()


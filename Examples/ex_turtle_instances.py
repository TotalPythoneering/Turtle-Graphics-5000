# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_turtle_instances.py
# AUTHOR: Randall Nagy
# ex_turtle_shapes.py
#
import turtle

# ex_turtle_instances
for ss, shape in enumerate(turtle.getshapes()):
    zt = turtle.Turtle()
    zt.up()
    zt.shape(shape)
    zt.forward(30 * ss)


for zt in turtle.turtles():
    zt.color('red')

turtle.done()


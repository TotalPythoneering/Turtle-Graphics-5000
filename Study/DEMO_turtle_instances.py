# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-19 12:48:40
# FILE: DEMO_turtle_instances.py
# AUTHOR: Randall Nagy
# DEMO_turtle_instances.py
#
import turtle

for ss, shape in enumerate(turtle.getshapes()):
    zt = turtle.Turtle() # instance creation
    zt.up()
    zt.shape(shape)
    zt.forward(30 * ss)

for zt in turtle.turtles():
    zt.color('red')

turtle.done()


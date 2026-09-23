# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-01 10:23:54
# FILE: DEMO_TurtleTicker.py
# AUTHOR: Randall Nagy
#
import turtle

turtle.shape("turtle")
turtle.shapesize(10)

def tilt_it():
    turtle.tilt(-10)
    turtle.ontimer(tilt_it, 250)

turtle.ontimer(tilt_it, 250)

turtle.listen()
turtle.done()


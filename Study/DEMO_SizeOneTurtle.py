# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-19 12:08:14
# FILE: DEMO_SizeOneTurtle.py
# AUTHOR: Randall Nagy
# DEMO_SizeOneTurtle.py
#
import turtle

zTurtle = False
print("1.1", turtle.turtlesize())
# Size the default Turtle
if zTurtle:
    print("1.2", turtle.turtlesize(12, 4, 3))
else:
    print("1.2", turtle.shapesize(12, 4, 3))

print("1.3", turtle.turtlesize())

# Make it look interesting
turtle.color('green')
turtle.fillcolor('gold')

turtle.done()



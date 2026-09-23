# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_12_robot_attributes.py
# AUTHOR: Randall Nagy
#
import turtle

# Default Robot Location
print(turtle.pos())
# Default Orientation
print(turtle.heading())
turtle.right(90)
print("NOW:", turtle.heading())

# Show the Pen's Attributes
pen = turtle.pen()
for ref in pen:
    print(ref, pen[ref])


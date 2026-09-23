# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-20 05:16:54
# FILE: LAB_stamp_delete.py
# AUTHOR: Randall Nagy
# LAB_stamp_delete.py
#
import turtle
import time

hold = turtle.color()
stamps = dict()
turtle.up(); turtle.goto(-200,0)
for shape in turtle.getshapes():
    if shape == 'blank':
        continue
    if shape is 'turtle':
        turtle.color('green', "yellow")
    else:
        turtle.color(hold[0], hold[1])
    turtle.shape(shape)
    stamps[shape] = turtle.stamp()
    turtle.forward(100)

for stamp in ('circle', 'square'):
    time.sleep(2.5)
    turtle.clearstamp(stamps[stamp])
    
turtle.done()


# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-19 13:50:56
# FILE: DEMO_stamp_delete.py
# AUTHOR: Randall Nagy
# DEMO_stamp_delete.py
#

import turtle

stamps = []
turtle.shape("turtle")
turtle.up(); turtle.goto(-200,0)
for ss in range(7):
    turtle.color('aqua')
    stamps.append(turtle.stamp())
    turtle.forward(50)

print("There are",
      len(turtle.turtles()),
      "robot instances")

for zt in stamps:
    import time
    time.sleep(0.25)
    turtle.clearstamp(zt)
    
turtle.bye()


# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-21 10:58:10
# FILE: DEMO_shape_tilt.py
# AUTHOR: Randall Nagy
# DEMO_shape_tilt.py
#
import turtle as xform

xform.hideturtle()
xform.width(3);xform.setpos(-400,0)
xform.color("gray");xform.shape("turtle")
xform.fillcolor("white")
xform.showturtle();xform.delay(100)
xform.shapesize(1,2,3)
for ref in range(9):
    xform.forward(70)
    xform.stamp()
    # xform.settiltangle(45) # consistent request = same view
    xform.tilt(45) # additive change
xform.hideturtle()

xform.mainloop()


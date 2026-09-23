# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_shearfactor.py
# AUTHOR: Randall Nagy
# ex_shearfactor.py
#
import turtle as xform

xform.hideturtle()
xform.penup()
xform.width(10)
xform.setpos(-400,0)
xform.color("gray")
xform.shape("turtle")
xform.showturtle()
xform.delay(0)
xform.shapesize(4,4,3)
xform.fillcolor("white")
xform.tilt(90)
for ref in range(6):
    xform.forward(100)
    xform.shearfactor(xform.shearfactor() + .13)
    xform.stamp()

xform.mainloop()


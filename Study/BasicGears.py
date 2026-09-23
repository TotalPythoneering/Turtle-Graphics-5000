# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-27 04:50:06
# FILE: BasicGears.py
# AUTHOR: Randall Nagy
#
import turtle

class SpikedGear:

    @staticmethod
    def draw_spike(base, high):
        clone = turtle.clone()
        clone.up()
        clone.right(180)
        clone.forward(base/2)
        p1 = clone.pos()
        clone.back(base)
        p2 = clone.pos()
        clone.forward(base/2)
        clone.right(90)
        clone.forward(high)
        p3 = clone.pos()
        
        turtle.goto(*p1)
        turtle.goto(*p3)
        turtle.goto(*p2)
        turtle.goto(*p1)

    @staticmethod        
    def draw_wheel(sides=6, length=100, base=20):
        turtle.home()
        half = base/2
        angle = (360/sides)
        if True:
            for ss in range(sides):
                turtle.goto(0,0)
                turtle.left(angle)
                SpikedGear.draw_spike(base, length)
                # Report
                dum = ss + 1
                print(dum, angle * dum)
        else:
            draw_spike(base, length)
        return True

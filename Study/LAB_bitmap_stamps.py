# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-20 07:17:08
# FILE: LAB_bitmap_stamps.py
# AUTHOR: Randall Nagy
# LAB_bitmap_stamps.py
#
import turtle
from StateSaver.EnumCircle import Enumerator as Enumerator

# file = "SeeTurtle.png"
file = "SeeTurtle.gif"

turtle.ht();turtle.up()
turtle.register_shape(file)

class Target:
    def __init__(self):
        self.times = 0

    def reset(self):
        self.times = 0
    
    def draw_turtle(self, angle, data):
        turtle.home()
        turtle.right(angle)
        turtle.forward(100)
        turtle.shape(data[self.times]['shape'])
        turtle.stamp()
        self.times += 1


values = (
    {'shape':file},
    {'shape':file},
    {'shape':file},
    {'shape':file}
    )

cntrl = Enumerator(len(values), degrees=360)

worker = Target()
cntrl.enum(worker.draw_turtle, values)


    
turtle.done()


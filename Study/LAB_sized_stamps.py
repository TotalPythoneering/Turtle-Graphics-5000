# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-20 07:24:18
# FILE: LAB_sized_stamps.py
# AUTHOR: Randall Nagy
# LAB_sized_stamps.py
#
import turtle
from StateSaver.EnumCircle import Enumerator as Enumerator

shape_name = "hershey"
points = ((9, 1), (7, 7), (7, 7), (1, 7), (1, 7),
(6, 11), (6, 11), (4, 17), (4, 17), (9, 13),
(9, 13), (14, 17), (14, 17), (12, 11), (12, 11),
(17, 7), (17, 7), (11, 7), (11, 7), (9, 1))

turtle.ht();turtle.up()
turtle.register_shape(shape_name, shape=points)

class SizedTarget:
    def __init__(self):
        self.times = 0

    def reset(self):
        self.times = 0
    
    def draw_turtle(self, angle, data):
        turtle.home()
        turtle.right(angle)
        turtle.forward(100)
        aspects = data[self.times]['size']
        turtle.shapesize(*aspects)
        turtle.shape(data[self.times]['shape'])
        turtle.stamp()
        self.times += 1

values = (
    {'shape':shape_name, "size":(10,10,0)},
    {'shape':shape_name, "size":(10,10,0)},
    {'shape':shape_name, "size":(10,10,0)},
    {'shape':shape_name, "size":(10,10,0)},
    )
if False:
    values = (
        {'shape':shape_name, "size":(1,1,1)},
        {'shape':shape_name, "size":(5,5,1)},
        {'shape':shape_name, "size":(15,5,1)},
        {'shape':shape_name, "size":(15,15,1)}
        )

cntrl = Enumerator(len(values), degrees=360)

worker = SizedTarget()
cntrl.enum(worker.draw_turtle, values)

    
turtle.done()


# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-21 01:48:58
# FILE: LAB_JosephsDiamond.py
# AUTHOR: Randall Nagy
# LAB_JosephsDiamond.py
#
import turtle

colors = ("red",'blue',"green","yellow")
points = ((0,30), (30,0), (0, -30), (-30, 0), (0, 30))

for color in colors:
    shape = turtle.Shape("compound")
    shape.addcomponent(points, color, "black")
    turtle.register_shape(color, shape)

def draw_shape(angle, data):
    turtle.up()
    turtle.shapesize(*data['size'])
    turtle.goto(data['pos'][0], data['pos'][1])
    turtle.shape(data['name'])
    return turtle.stamp()
    
values = [
    {'name':'red', 'pos':(100,100), 'size':(3, 3, 1)},
    {'name':'blue', 'pos':(-100,100), 'size':(4, 4, 2)},
    {'name':'green', 'pos':(100,-100), 'size':(5, 5, 3)},
    {'name':'yellow', 'pos':(-100,-100), 'size':(6, 6, 4)}
    ]

for dat in values:
    if True:
        dat['size'] = (3, 3, 3)
    draw_shape(None, dat)
    
turtle.mainloop()


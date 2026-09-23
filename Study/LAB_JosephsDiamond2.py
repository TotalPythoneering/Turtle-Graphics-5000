# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-21 01:53:08
# FILE: LAB_JosephsDiamond2.py
# AUTHOR: Randall Nagy
# LAB_JosephsDiamond2.py
#
import turtle

def get_circle():
    robot = turtle.Turtle();
    robot.ht()
    robot.begin_poly()
    robot.color("aqua") # Pen Ignored
    robot.circle(10)
    robot.end_poly()
    points = robot.get_poly()
    # print(points)
    robot.clear()
    return points

colors = ("red",'blue',"green","yellow")
points = ((0,30), (30,0), (0, -30), (-30, 0), (0, 30))
circle = get_circle()

for color in colors:
    shape = turtle.Shape("compound")
    shape.addcomponent(points, color, "black")
    shape.addcomponent(circle, 'white', "black")
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
    if False:
        dat['size'] = (3, 3, 3)
    draw_shape(None, dat)
    
turtle.mainloop()


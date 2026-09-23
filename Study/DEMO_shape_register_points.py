# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-20 10:08:16
# FILE: DEMO_shape_register_points.py
# AUTHOR: Randall Nagy
# DEMO_shape_register_points.py
# External files neither scale, nor rotate, nor do "pen-things."
#
import turtle

turtle.ht();turtle.up()
shape_name = "LandTurtle.gif"
if True:
    shape_name = "hershey"
    points = ((9, 1), (7, 7), (7, 7), (1, 7), (1, 7),
    (6, 11), (6, 11), (4, 17), (4, 17), (9, 13),
    (9, 13), (14, 17), (14, 17), (12, 11), (12, 11),
    (17, 7), (17, 7), (11, 7), (11, 7), (9, 1))
    turtle.register_shape(shape_name, shape=points)
else:
    turtle.register_shape(shape_name)

turtle.goto(-300,200)
turtle.shape(shape_name)
turtle.stamp()
turtle.color('gold','blue')
turtle.shapesize(6, 12, 10)
turtle.forward(200); turtle.left(-45)
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)

turtle.done()


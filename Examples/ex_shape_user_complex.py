# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_shape_user_complex.py
# AUTHOR: Randall Nagy
# ex_shape_user_complex.py
#
import turtle

shape = turtle.Shape("compound")
pointsA = ((30,-30), (0,5), (-30,-30))
pointsB = ((60,-60), (0,10), (-60,-60))
shape.addcomponent(pointsB, "gray", "black")
shape.addcomponent(pointsA, "gold", "green")
turtle.register_shape("MyComplexTriangle", shape)
turtle.shape("MyComplexTriangle")
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)

turtle.done()


# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_shape_register_gif.py
# AUTHOR: Randall Nagy
# ex_shape_register_gif.py
#
import turtle


turtle.register_shape("MyImage.gif")

turtle.shape("MyImage.gif")
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)

turtle.done()


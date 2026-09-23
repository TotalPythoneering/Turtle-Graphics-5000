# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_35_shape_user_tuple.py
# AUTHOR: Randall Nagy
#

import turtle

turtle.register_shape("MyTriangle", ((30,-30), (0,5), (-30,-30)))
turtle.shape("MyTriangle")
turtle.color('aqua') # color our shape
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)



turtle.done()


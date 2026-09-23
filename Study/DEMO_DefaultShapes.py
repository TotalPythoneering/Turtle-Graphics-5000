# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-19 11:48:38
# FILE: DEMO_DefaultShapes.py
# AUTHOR: Randall Nagy
# DEMO_DefaultShapes.py
#

import turtle
import time

for shape in turtle.getshapes():
    turtle.clear()
    turtle.up()
    turtle.goto(-20, -50); turtle.write(shape)
    turtle.home()
    turtle.shape(shape) # registry name
    turtle.showturtle()
    time.sleep(3)
    

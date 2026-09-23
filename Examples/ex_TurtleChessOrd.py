# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_TurtleChessOrd.py
# AUTHOR: Randall Nagy
#
import turtle

turtle.setup(800, 800)
turtle.up()
turtle.goto(-300, 300)
for ss in range(9812, 9824):
    turtle.write(chr(ss), font=('Ariel', 48, 'normal'))
    turtle.forward(48)


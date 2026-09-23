# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_02_cartesian.py
# AUTHOR: Randall Nagy
#

# Turtle Graphics in Python 3
import turtle

# .home() <> .goto(0,0)
for line in range(4):
    turtle.left(90)
    turtle.forward(100)
    turtle.goto(0,0)

# Same as mainloop()
turtle.done()



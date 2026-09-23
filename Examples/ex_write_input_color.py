# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:58
# FILE: ex_write_input_color.py
# AUTHOR: Randall Nagy
#

for ss in range(100):
    print() #  clear the screen

import turtle

data = turtle.textinput("Get String", "Color:")

if data is not None:
    turtle.color(data)
    turtle.write("This is the color!")
    



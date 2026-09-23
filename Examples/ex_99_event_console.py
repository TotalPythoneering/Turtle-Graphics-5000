# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_99_event_console.py
# AUTHOR: Randall Nagy
#

import turtle as screen

screen.screensize(800, 600)
screen.setworldcoordinates(0, 600, 600, 0)

colors = ("red", "yellow", "pink",
          "blue", "aqua", "green")

icolor = len(colors)

def zoom():
    global icolor, colors
    icolor += 1
    if(icolor >= len(colors)):
        icolor = 0
    screen.dot(100, colors[icolor])

controls = dict()
screen.hideturtle()
screen.delay(0)
screen.penup()
screen.goto(300,300)
screen.dot(100, 'green')

screen.onkey(zoom, "c")

screen.listen()

screen.mainloop()

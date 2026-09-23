# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-25 11:40:00
# FILE: DEMO_onkey.py
# AUTHOR: Randall Nagy
# DEMO_onkey.py
#
import turtle as screen

colors = ("red", "yellow", "pink",
          "blue", "aqua", "green")
icolor = len(colors)

def quit():
    screen.bye()

def zoom():
    global icolor, colors
    icolor += 1
    if(icolor >= len(colors)):
        icolor = 0
    screen.dot(100, colors[icolor])

screen.hideturtle()
screen.delay(0)
screen.penup()
screen.dot(100, 'green')

screen.onkey(zoom, "c")
screen.onkey(quit, "q")

screen.listen()

screen.mainloop()




# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-25 15:32:28
# FILE: DEMO_ontimer.py
# AUTHOR: Randall Nagy
# DEMO_ontimer
#
import turtle as screen

colors = ("red", "yellow", "pink",
          "blue", "aqua", "green")
icolor = len(colors)

def quit():
    screen.ontimer(tick, 0) # cancel
    screen.bye()

def tick():
    global icolor, colors
    icolor += 1
    if(icolor >= len(colors)):
        icolor = 0
    screen.dot(100, colors[icolor])
    # Re-Schedule Callback
    screen.ontimer(tick, 1000)

screen.hideturtle()
screen.delay(0)
screen.penup()

screen.onkey(quit, "q")
screen.ontimer(tick, 1000)

screen.listen()
screen.done() # required!


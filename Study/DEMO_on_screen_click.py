# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-27 07:04:32
# FILE: DEMO_on_screen_click.py
# AUTHOR: Randall Nagy
# DEMO_on_screen_click.py
#
import turtle as screen

colors = ("red", "yellow", "pink",
          "blue", "aqua", "green")
icolor = len(colors) - 1

def quit():
    screen.bye()

def color(ignored1, ignored2):
    global icolor, colors
    icolor += 1
    if(icolor >= len(colors)):
        icolor = 0
    screen.goto(0,0)
    screen.dot(100, colors[icolor])

def click(xpos, ypos):
    screen.goto(xpos, ypos)
    screen.dot(50, colors[icolor])
    print(xpos, ypos)


screen.hideturtle()
screen.delay(0)
screen.penup()
color(None, None)

screen.onkey(quit, "q")
screen.onscreenclick(click, btn=1, add=True)
screen.onscreenclick(color, btn=3, add=True)

screen.listen()
screen.mainloop()


# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-27 05:18:12
# FILE: LAB_Spiked_Gears2.py
# AUTHOR: Randall Nagy
# LAB_Spiked_Gears2.py
#
import turtle


# Modeling Parameters
zLength = 90; zBase = 20
num_msec = 100
data = [
    {"sides":6, "length":zLength, "base":zBase},
    {"sides":12, "length":zLength, "base":zBase}
    ]
zSet = (turtle.Turtle(), turtle.Turtle())

def quit():
    turtle.bye()

def on_timed_event():
    zSet[0].tilt(2)
    zSet[1].tilt(-2)
    turtle.ontimer(on_timed_event, num_msec)

# Initialization
turtle.speed(0);turtle.delay(0)
turtle.penup();turtle.hideturtle()

# Re-use - Class from file in `pwd`
from BasicGears import SpikedGear

# Create simulation
for ss in range(len(zSet)):
    name = "MyGear" + str(ss)
    turtle.begin_poly()
    SpikedGear.draw_wheel(**(data[ss]))
    turtle.end_poly()
    shape = turtle.Shape("polygon", turtle.get_poly())
    turtle.register_shape(name, shape)
    zTurtle = zSet[ss]
    zTurtle.shape(name)
    zTurtle.color("gray", "gray")
    zTurtle.showturtle()
    zTurtle.penup()

# Setup display
turtle.goto(0, 200)
turtle.color('BLUE')
turtle.write("SPIKED GEARS IN-ACTION", font=("Arial", 24, "normal"), align='center')
xpos = zLength - zBase
zSet[0].goto(xpos, zLength)
zSet[1].goto(-xpos, xpos)

# Schedule event
turtle.onkey(quit, "q")
turtle.ontimer(on_timed_event, num_msec)

# Start framework
turtle.listen()

# Wait for stopage
turtle.mainloop()


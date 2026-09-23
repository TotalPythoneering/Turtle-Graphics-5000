# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-29 08:52:08
# FILE: DEMO_BasicGears2.py
# AUTHOR: Randall Nagy
# DEMO_BasicGears2.py
#
import turtle


# Modeling Parameters
zLength = 100; zBase = 20
num_msec = 100
data = [
    {"sides":8, "length":zLength, "base":zBase, "line":"black", "fill":"black"},
    {"sides":16, "length":zLength, "base":zBase, "line":"blue", "fill":"blue"}
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
from BasicGears2 import SpikedGear

# Create simulation
for ss, zTurtle in enumerate(zSet):
    name = "MyGear" + str(ss)
    zdat = data[ss]
    gear = SpikedGear(length=zdat["length"], base=zdat["base"])
    shape = gear.create_shape(zdat["sides"], line=zdat["line"], fill=zdat["fill"], hole=True)
    turtle.register_shape(name, shape)
    zTurtle.shape(name)
    zTurtle.showturtle()
    zTurtle.penup()

# Setup display
turtle.goto(0, 200)
turtle.color('green')
turtle.write("SHARP GEARS IN-ACTION", font=("Arial", 24, "normal"), align='center')
xpos = zLength - zLength / 3
zSet[0].goto(xpos, -xpos)
zSet[1].goto(-xpos, xpos)

# Schedule event
turtle.onkey(quit, "q")
turtle.ontimer(on_timed_event, num_msec)

# Start framework
turtle.listen()

# Wait for stopage
turtle.mainloop()


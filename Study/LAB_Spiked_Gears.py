# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-28 04:46:02
# FILE: LAB_Spiked_Gears.py
# AUTHOR: Randall Nagy
# LAB_Spiked_Gears.py
#
import turtle


# Modeling Parameters
num_msec = 100
data = {"sides":8, "length":80, "base":20}
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

# Draw Shape / Gear
turtle.begin_poly()
ok = SpikedGear.draw_wheel(**data)
turtle.end_poly()

# Extract & Register Shape
shape = turtle.Shape("polygon", turtle.get_poly())
turtle.register_shape("MyGear", shape)

# Create simulation
for ss in range(len(zSet)):
    zTurtle = zSet[ss]
    zTurtle.shape("MyGear")
    zTurtle.color("gray", "gray")
    zTurtle.showturtle()
    zTurtle.penup()

# Setup display
turtle.goto(0, 200)
turtle.color('BLUE')
turtle.write("SPIKED GEAR IN-ACTION", font=("Arial", 24, "normal"), align='center')
xpos = data["length"] - data["base"]
zSet[0].goto(xpos, data["length"])
zSet[1].goto(-xpos, xpos)

# Schedule event
turtle.onkey(quit, "q")
turtle.ontimer(on_timed_event, num_msec)

# Start framework
turtle.listen()

# Wait for stopage
turtle.mainloop()


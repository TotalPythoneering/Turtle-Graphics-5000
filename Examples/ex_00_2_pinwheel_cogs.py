# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_00_2_pinwheel_cogs.py
# AUTHOR: Randall Nagy
# Duplicate file. Primary file elsewhere.
#

import turtle

zSet = (turtle.Turtle(), turtle.Turtle())

num_msec = 100

def quit():
    turtle.bye()

def zoom():
    zSet[0].tilt(2)
    zSet[1].tilt(-2)
    turtle.ontimer(zoom, num_msec)

def draw_pin_wheel(zSlices=10, zRange=100, zBite=-1):
    angle = int(360 / zSlices)
    locs = [[[-1 for z in range(1)] for y in range(2)] for x in range(zSlices + 1)]
    if zBite <=0:
        zBite = int(zRange / 10)

    zLine = 0
    for ref in range(len(locs)):
        turtle.left(angle)
        turtle.forward(zRange)
        locs[zLine][1] = turtle.pos()
        turtle.back(zBite)
        locs[zLine][0] = turtle.pos()
        turtle.goto(0, 0)
        print(locs[zLine])
        zLine += 1

    turtle.home()
    for line in range(len(locs)):
        listA = locs[line][0]
        turtle.goto(listA[0], listA[1]) # Key Point
        listB = locs[0][1]
        if line < (zSlices - 1):
            listB = locs[line + 1][1]
        # Cut-draw the outer 'cut'
        turtle.goto(listB[0], listB[1]) # Cog-Angle
        turtle.goto(listA[0], listA[1]) # Inner-Polygon


turtle.hideturtle()
turtle.delay(0)
turtle.penup()

# Create cog
turtle.penup()
turtle.begin_poly()
turtle.hideturtle()
draw_pin_wheel(zSlices=60, zRange=100, zBite=30)
turtle.end_poly()

colors = ("black", "black")
for index in range(len(zSet)):
    shape = turtle.Shape("compound")
    points = turtle.get_poly()
    shape.addcomponent(points, colors[index], 'black')
    turtle.register_shape("MyPinwheel" + str(index), shape)

for ss in range(len(zSet)):
    zTurtle = zSet[ss]
    zTurtle.shape("MyPinwheel" + str(ss))
    zTurtle.showturtle()
    zTurtle.penup()

turtle.goto(0, 200)
turtle.color('green')
turtle.write("PINWHEEL COGS IN-ACTION", font=("Arial", 24, "normal"), align='center')
zSet[0].goto(90, 100)
zSet[1].goto(-90, 97)

# Schedule event
turtle.onkey(quit, "q")
turtle.ontimer(zoom, num_msec)

turtle.listen()

turtle.mainloop()



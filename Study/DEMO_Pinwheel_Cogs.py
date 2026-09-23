# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-26 04:32:24
# FILE: DEMO_Pinwheel_Cogs.py
# AUTHOR: Randall Nagy
# DEMO_Pinwheel_Cogs.py
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


# Return False if the number of slices will not work (e.g 7, 14, 16, etc.)
def draw_pin_wheel(zTurtle=turtle, zSlices=10, zRange=100, zBite=-1):
    # Check for hgte 'pi problem'
    if 360 % zSlices:
       return False

    angle = int(360 / zSlices)
    locs = [[[None for z in range(1)] for y in range(2)] for x in range(zSlices + 1)]
    if zBite <= 0:
        zBite = int(zRange / 10)

    zSize = len(locs)
    zLine = 0
    for ref in range(zSize):
        zTurtle.left(angle)
        zTurtle.forward(zRange)
        locs[zLine][1] = zTurtle.pos()
        zTurtle.back(zBite)
        locs[zLine][0] = zTurtle.pos()
        zTurtle.goto(0, 0)
        print(locs[zLine])
        zLine += 1

    turtle.home()
    # Demonstrative - let's keep it sane 4 others =)
    for line in range(zSize):
        listA = locs[line][0]
        zTurtle.goto(listA[0], listA[1])  # Key Point
        listB = locs[0][1]
        if line < (zSize - 1):
            listB = locs[line + 1][1]

        # Cut-draw the outer 'cut'
        zTurtle.goto(listB[0], listB[1])  # Cog-Angle
        zTurtle.goto(listA[0], listA[1]) # Inner-Polygon

    return True

turtle.hideturtle()
turtle.delay(0)
turtle.penup()

# Create cog
turtle.penup()
turtle.begin_poly()
turtle.hideturtle()
ok = draw_pin_wheel(zSlices=10, zRange=100, zBite=30)
if not ok:
    print("Bad Slice")
    turtle.bye()

turtle.end_poly()

shape = turtle.Shape("compound")
points = turtle.get_poly()
shape.addcomponent(points, "black", "black")
turtle.register_shape("MyPinwheel", shape)

for ss in range(len(zSet)):
    zTurtle = zSet[ss]
    zTurtle.shape("MyPinwheel")
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


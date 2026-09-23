# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_00_3_pinwheel_cogs.py
# AUTHOR: Randall Nagy
# Duplicate file. Primary file elsewhere.
#

import turtle

num_msec = 100


def quit():
    turtle.bye()


def zoom():
    zSet[0].tilt(2)
    zSet[1].tilt(-2)
    zSet[2].tilt(2)
    turtle.ontimer(zoom, num_msec)

# Determine if our slice choice will work
def is_cardnal(slices):
    return 360 % slices is 0

# Return False if the number of slices will not work (e.g 7, 14, 16, etc.)
def draw_pin_wheel(zTurtle=turtle, zSlices=10, zRange=100, zBite=-1):
    # Check for hgte 'pi problem'
    if 360 % zSlices is not 0:
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


class TurtleShape(turtle.Turtle):
    def __init__(self, zShape='default', zSlices=10, zRange=100, zBite=-1):
        super().__init__()
        self.zShape = zShape
        self.zSlices = zSlices
        self.zRange = zRange
        self.zBite = zBite

    def assign_shape(self):
        self.penup()
        self.begin_poly()
        self.hideturtle()
        draw_pin_wheel(zTurtle=self, zSlices=self.zSlices, zRange=self.zRange, zBite=self.zBite)
        self.end_poly()

        shape = turtle.Shape("compound")
        points = self.get_poly()
        shape.addcomponent(points, 'black', 'black')
        turtle.register_shape(self.zShape, shape)
        self.shape(self.zShape)

zSet = (
    TurtleShape(zShape="large", zSlices=15, zRange=100, zBite=30),
    TurtleShape(zShape="medium", zSlices=10, zRange=80, zBite=30),
    TurtleShape(zShape="small", zSlices=5, zRange=60, zBite=30)
)

zPoints = (
    (153, 105),
    (-20, 96),
    (-151, 109)
)

turtle.hideturtle()
turtle.delay(0)
turtle.penup()


turtle.goto(0, 240)
turtle.color('green')
turtle.write("PINWHEELS: GEAR SIMULATION", font=("Arial", 24, "normal"), align='center')

for index in range(len(zSet)):
    zSet[index].penup()
    zSet[index].hideturtle()
    zSet[index].assign_shape()
    zSet[index].goto(zPoints[index][0], zPoints[index][1])
    zSet[index].showturtle()

turtle.goto(0, -50)
# turtle.write("N+1 GEARING (5, 6, 8)", font=("Arial", 24, "normal"), align='center')

turtle.goto(115, -90)
turtle.write("Vectors on Python (Cartesian 'Turtle Graphics')", font=("Arial", 8, "normal"), align='center')

# Schedule event
turtle.onkey(quit, "q")
turtle.ontimer(zoom, num_msec)

turtle.listen()

turtle.mainloop()

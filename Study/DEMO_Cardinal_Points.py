# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-26 04:42:42
# FILE: DEMO_Cardinal_Points.py
# AUTHOR: Randall Nagy
# DEMO_Cardinal_Points.py
#
import turtle


'''
We need to be slightly more careful with the parameters here than in our
other demonstrations - the entire point of this rendition is to create a
3-dimensional array of points that can be used for 'zBite' calculations.

The use of Cardinal slice-values is important!
(see post at http://soft9000.com/blog9000/index.php?entry=entry170122-020104)

For things to work properly, we must therefore be sure that zStep <> zRange,
as well as that zStep < zRange. Since this is an academic demo, in order
to make things a tad cleaner to read, we removed our in-code parameter
checks.
'''
def draw_pin_wheel(zSlices=10, zRange=100, zBite=-1, zSmile=False):
    zt = turtle.Turtle(shape='turtle')
    angle = int(360 / zSlices)
    locs = [[[-1 for z in range(1)] for y in range(2)] for x in range(zSlices)]
    if zBite <=0:
        zBite = int(zRange / 10)

    zLine = 0
    zt.hideturtle()
    for ref in range(1, 360, angle):
        zt.left(angle)
        zt.forward(zRange)
        zt.circle(1)
        locs[zLine][1] = zt.pos()
        zt.back(zBite)
        locs[zLine][0] = zt.pos()
        zt.circle(1)
        zt.goto(0, 0)
        print(locs[zLine])
        zLine += 1

    if zSmile:
        zt.home()
        zt.begin_fill()
        for line in range(len(locs)):
            zt.penup()
            listA = locs[line][0]
            zt.goto(listA[0], listA[1])
            zt.pendown()
            listB = locs[0][0]
            if line < zSlices - 1:
                listB = locs[line + 1][0]
            # Hex-draw the inner 'circle'
            zt.goto(listB[0], listB[1])
            zt.goto(listA[0], listA[1])
        zt.end_fill()

    zt.home()
    zt.color('red')
    for line in range(len(locs)):
        zt.penup()
        listA = locs[line][0]
        zt.goto(listA[0], listA[1])
        zt.pendown()
        listB = locs[0][1]
        if line < zSlices - 1:
            listB = locs[line + 1][1]
        # Cut-draw the outer 'cut'
        zt.goto(listB[0], listB[1])
        zt.goto(listA[0], listA[1])

    zt.penup()
    zt.color('black')
    zLoc = zRange + zBite
    zt.goto(zLoc * -1, zLoc)
    zt.write("draw_pin_wheel(zSlices=" + str(zSlices) + ", zRange=" + str(zRange) + ", zBite=" + str(zBite) + ")")
    zt.hideturtle()

turtle.hideturtle()
draw_pin_wheel(zSlices=10, zRange=100, zBite=30, zSmile=True)
turtle.getscreen()._root.mainloop()

# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:19:26
# FILE: ex_shapetransform.py
# AUTHOR: Randall Nagy
# ex_shapetransform.py
#
import turtle


def create():
    turtle.reset()
    turtle.clear()
    turtle.up()
    turtle.goto(0, -200)
    turtle.ht()
    turtle.width(5)
    turtle.shape("circle")
    return turtle

def draw_cartx(turtle, sz=200):
    turtle.ht();turtle.down()
    pos = turtle.pos()
    turtle.color('gray')
    for angle in (0, 90, 180, 270, 360, 180):
        turtle.left(angle)
        turtle.forward(sz/2)
        turtle.goto(pos[0], pos[1])
    turtle.goto(pos[0], pos[1] - sz/4)
    turtle.circle(sz/4)
    turtle.goto(pos[0], pos[1])
    turtle.color('black')
    turtle.up()

def vround(values):
    results = []
    for points in values:
        line = []
        for ss, val in enumerate(points):
            line.append(round(val, 2))
        results.append(line)
    return results

def report(values):
    values = vround(values)
    font=("Ariel", 24, "normal")
    t1 = create();t1.showturtle()
    pos = t1.pos()
    turtle.up()
    for ss, val in enumerate(values):
        zy = pos[1] + (130 * ss)
        t1.goto(pos[0], zy)
        t1.shapetransform(*val)
        t1.stamp()
        draw_cartx(t1)
        t1.goto(pos[0]+125, zy - 20)
        t1.write(t1.shapetransform(), font=font)
        t1.goto(pos[0], pos[1])
    import time
    time.sleep(5)

case = 2
if case is 0:
    t1 = create()
    t1.shapetransform(1, 1, 1, 1)   
elif case is 1:
    t1 = turtle.Turtle()
    print("Default:", t1.shapetransform())
    t1.shearfactor(-0.5)
    print("\t shearfactor(-0.5):\t\t",
          t1.shapetransform())

    t1 = create()
    t1.shapetransform(-1, -2, 2, 1)
    print("\t shapetransform:(-1, -2, 2, 1)\t",
          t1.shapetransform())
    print('~' * 10)
elif case is 2:
    t1 = create()
    t1.speed(0);t1.delay(0)
    values = ((1,0,0,1),(3,0,0,3),(5,0,0,5))
    report(values)
    big = 5; base=4
    values = ((big,base,0,big),(big,base-1,0,big),
          (big,base-2,0,big))
    report(values)
    values = ((big,0,base,big),(big,0,base-1,big),
         (big,0,base-2,big))
    report(values)
    values = ((big,base,base,big),(big,base-1,base-1,big),
          (big,base-2,base-2,big))
    report(values)






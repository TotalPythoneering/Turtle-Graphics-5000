# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-24 07:19:42
# FILE: LAB_shapetransform.py
# AUTHOR: Randall Nagy
# LAB_shapetransform.py
#
import turtle

def create():
    turtle.reset()
    turtle.clear()
    turtle.up()
    turtle.goto(0, -200)
    turtle.ht()
    turtle.width(5)
    turtle.shape("turtle")
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

def report(values):
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

t1 = create()
big = 6
values = ((big,0,0,-big),(big,0,-big,big),(big,-big,0,big))
report(values)






# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-24 06:43:42
# FILE: LAB_TurtleCoin.py
# AUTHOR: Randall Nagy
# LAB_TurtleCoin.py
#
import turtle

def draw_tilted(angle, data):
    turtle.up()
    turtle.home()
    turtle.color(*data['color'])
    turtle.goto(data['pos'][0], data['pos'][1])
    turtle.shape(data['name'])
    turtle.shapesize(*data['size'])
    # Post-HOME (directive, else additive - and slower!)
    #turtle.left(angle)

    turtle.settiltangle(angle)
    return turtle.stamp()

zcoin =  (20,20,7)
zsize = (zcoin[0]/4,zcoin[1]/4,zcoin[2]/2)
values = [
    {'name':'turtle', 'color':('black', 'red'), 'size':zsize,'pos':(0,100)},
    {'name':'turtle', 'color':('black', 'green'), 'size':zsize,'pos':(-100,0)},
    {'name':'turtle', 'color':('black', 'white'), 'size':zsize,'pos':(0,-100)},
    {'name':'turtle', 'color':('black', 'aqua'), 'size':zsize,'pos':(100,0)}
    ]

from StateSaver.EnumCircle import Enumerator

turtle.ht();turtle.up()
turtle.shape('circle')
turtle.color('gold', 'blue')
turtle.shapesize(*zcoin)
turtle.stamp()
faces = Enumerator(len(values))
for ss, angle in enumerate(faces.next()):
    draw_tilted(angle, values[ss])
    
turtle.mainloop()


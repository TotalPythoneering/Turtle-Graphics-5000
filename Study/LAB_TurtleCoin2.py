# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-23 08:18:00
# FILE: LAB_TurtleCoin2.py
# AUTHOR: Randall Nagy
# LAB_TurtleCoin2.py
#
import turtle

def draw_tilted(angle, data):
    turtle.up()
    turtle.home()
    turtle.color(*data['color'])
    turtle.goto(data['pos'][0], data['pos'][1])
    turtle.shape(data['name'])
    turtle.shapesize(*data['size'])
    turtle.settiltangle(angle)
    turtle.shearfactor(data['sf']) # Simple co-existance
    return turtle.stamp()

zcoin =  (20,20,7)
logo = (zcoin[0]/4,zcoin[1]/4,zcoin[2]/2)
values = [
    {'sf':0, 'name':'turtle', 'color':('black', 'red'), 'size':logo,'pos':(0,100)},
    {'sf':0.33, 'name':'turtle', 'color':('black', 'green'), 'size':logo,'pos':(-100,0)},
    {'sf':0.66, 'name':'turtle', 'color':('black', 'white'), 'size':logo,'pos':(0,-100)},
    {'sf':1, 'name':'turtle', 'color':('black', 'aqua'), 'size':logo,'pos':(100,0)}
    ]

from StateSaver.EnumCircle import Enumerator

turtle.ht();turtle.up()
turtle.shape('circle')
turtle.color('gold', 'blue')
turtle.shapesize(*zcoin)
turtle.stamp()
faces = Enumerator(len(values)) #, degrees=360/len(values))
for ss, angle in enumerate(faces.next()):
    draw_tilted(angle, values[ss])
    #tilt_and_go(angle, values[ss])
    
turtle.mainloop()


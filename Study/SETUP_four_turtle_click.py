# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-06 04:19:38
# FILE: SETUP_four_turtle_click.py
# AUTHOR: Randall Nagy
# SETUP_four_turtle_click.py
#
import turtle

colors = ('red', 'green', 'blue', 'gold')
shapes = ('turtle', 'arrow', 'square', 'classic', 'triangle')


class TurtleInstance(turtle.Turtle):

    def __init__(self, xpos, ypos):
        pass

    def setup_turtle(self, xpos, ypos):
        pass

    # Change the turtle's color
    def change_color(self, xcord, ycord):
        pass

    # Change the turtle's fill color
    def change_fill(self, xcord, ycord):
        pass

    # Enumerate thru the shapes
    def change_shape(self, xcord, ycord):
        pass

    # Rotate 45 degrees
    def change_directon(self, xcord, ycord):
        pass


zSet = (TurtleInstance(-100, 100),
        TurtleInstance(100, -100),
        TurtleInstance(-100, -100),
        TurtleInstance(100, 100))

func = (zSet[0].change_color,
        zSet[1].change_fill,
        zSet[2].change_shape,
        zSet[3].change_directon)

# Setup response event for each instance
for num in range(len(zSet)):
    zSet[num].onclick(func[num])

turtle.done()



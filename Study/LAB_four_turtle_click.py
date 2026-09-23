# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-06 04:18:46
# FILE: LAB_four_turtle_click.py
# AUTHOR: Randall Nagy
# LAB_four_turtle_click.py
#
import turtle

colors = ('red', 'green', 'blue', 'gold')
shapes = ('turtle', 'arrow', 'square', 'classic', 'triangle')


class TurtleInstance(turtle.Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        super().shape('turtle') # PEP 3135
        self.index = 0
        self.setup_turtle(xpos, ypos)

    def setup_turtle(self, xpos, ypos):
        self.penup()
        self.shapesize(4, 4, 7)
        self.fillcolor(colors[self.index])
        self.goto(xpos, ypos)

    # Change the turtle's color
    def change_color(self, xcord, ycord):
        self.index += 1
        if self.index >= len(colors):
            self.index = 0
        self.color(colors[self.index])
        print("change_color(" + str(self.color()) +")")

    # Change the turtle's fill color
    def change_fill(self, xcord, ycord):
        self.index += 1
        if self.index >= len(colors):
            self.index = 0
        self.fillcolor(colors[self.index])
        print("change_fill(" + str(self.fillcolor()) +")")

    # Enumerate thru the shapes
    def change_shape(self, xcord, ycord):
        self.index += 1
        if self.index >= len(shapes):
            self.index = 0
        self.shape(shapes[self.index])
        print("change_shape(" + str(self.shape()) +")")

    # Rotate 45 degrees
    def change_directon(self, xcord, ycord):
        self.tilt(45)
        print("change_directon(" + str(45) + ")")


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



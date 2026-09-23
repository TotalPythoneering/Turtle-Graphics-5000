# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-06 04:06:54
# FILE: DEMO_four_turtle_click.py
# AUTHOR: Randall Nagy
# DEMO_four_turtle_click.py
#
import turtle

colors = ('red', 'green', 'blue', 'gold')

class TurtleInstance(turtle.Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        super().shape('turtle') # PEP 3135
        self.index = 0
        self.goto(xpos, ypos)
        self.penup()
        self.shapesize(4, 4, 7)
        self.fillcolor(colors[self.index])
        self.onclick(self.on_click)

    # Change the turtle's color
    def on_click(self, xcord, ycord):
        self.index += 1
        if self.index >= len(colors):
            self.index = 0
        self.color(colors[self.index])
        print("Instance:", id(self), "clicked.")


zSet = (TurtleInstance(-100, 100),
        TurtleInstance(100, -100),
        TurtleInstance(-100, -100),
        TurtleInstance(100, 100)
        )

# turtle.listen()
turtle.done()



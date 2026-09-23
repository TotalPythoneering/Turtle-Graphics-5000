# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-25 12:42:08
# FILE: LAB_onkey2.py
# AUTHOR: Randall Nagy
# LAB_onkey2.py
#
import turtle as screen


class OnKey:
    colors = ("red", "green", "aqua", "blue")
    
    def __init__(self):
        self.shapes = screen.getshapes()
        self.shapes.remove("blank")
        self.ishape = len(self.shapes) - 1
        screen.shape(self.shapes[self.ishape])
        
        self.icolor = len(OnKey.colors) - 1
        screen.color("black", OnKey.colors[self.icolor])
        screen.onkey(self.toggle_shape, "t")
        screen.onkey(self.zoom, "z")
        screen.onkey(self.color, "c")
        screen.onkey(self.quit, "q")

        screen.onscreenclick(self.stamp, btn=1, add=True)
    
    def quit(self):
        screen.bye()

    def stamp(self, xpos, ypos):
        screen.goto(xpos, ypos)
        screen.stamp()
        screen.home()

    def toggle_shape(self):
        self.ishape += 1
        if self.ishape >= len(self.shapes):
            self.ishape = 0
        screen.shape(self.shapes[self.ishape])

    def zoom(self):
        zsize = list(screen.shapetransform())
        if zsize[0] > 20:
            zsize[0] = zsize[3] = 1
        else:
            zsize[0] = zsize[3] = zsize[0] + 2
        screen.shapetransform(*zsize)

    def color(self):
        self.icolor += 1
        if(self.icolor >= len(OnKey.colors)):
            self.icolor = 0
        screen.color("black", OnKey.colors[self.icolor])

screen.penup()
screen.speed(0);screen.delay(0)
lab = OnKey()
screen.listen()





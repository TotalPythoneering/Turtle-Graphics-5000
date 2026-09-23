# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-29 08:45:22
# FILE: BasicGears2.py
# AUTHOR: Randall Nagy
# BasicGears2.py
#
import turtle

class SpikedGear:

    def __init__(self, zt=turtle.Turtle(), length=80, base=40):
        self.robot = zt
        self.length = length
        self.base = base
        self.robot.ht();self.robot.up()
        self.p1 = self.p2 = self.p3 = None
        self.hole = False

    def draw_spike(self, base, high):
        clone = self.robot.clone()
        clone.right(180)
        clone.forward(base/2)
        self.p1 = clone.pos()
        clone.back(base)
        self.p2 = clone.pos()
        clone.forward(base/2)
        clone.right(90)
        clone.forward(high)
        self.p3 = clone.pos()

        self.robot.goto(*self.p1)
        self.robot.goto(*self.p3)
        self.robot.goto(*self.p2)
        self.robot.goto(*self.p1)

    def circle_pos(self, size):
        self.robot.goto(0, -size)
        self.robot.circle(size)

    def on_final(self, shape):
        ''' Chance to add more polygons (.addcomponent) the final turtle.Shape '''
        if self.hole:
            self.robot.goto(0,0)
            self.robot.begin_poly()
            self.circle_pos(1)
            self.robot.end_poly()
            shape.addcomponent(self.robot.get_poly(), "white", "white")
      
    def create_shape(self, sides, line="black", fill="black", fract=False, hole=False):
        import turtle
        shape = turtle.Shape("compound")
        self.robot.home()
        self.hole = hole
        angle = (360/sides)
        
        self.robot.home()
        for ss in range(sides):
            self.robot.begin_poly()
            if fract is False:
                self.robot.goto(0,0)
            self.robot.left(angle)
            self.draw_spike(self.base, self.length)
            self.robot.end_poly()
            shape.addcomponent(self.robot.get_poly(), fill, line)

        self.on_final(shape)
        
        return shape


if __name__ == "__main__":
    print("Creating...")
    turtle.ht()
    gear = SpikedGear()
    shape = gear.create_shape(3, line="black", fract=False, hole=True)
    print("Created", shape)
    turtle.register_shape("MySpike", shape)
    turtle.shape("MySpike")
    turtle.stamp()

# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-25 15:31:44
# FILE: LAB_ontimer.py
# AUTHOR: Randall Nagy
# LAB_ontimer
#
import turtle as screen


class Clocker:
    def __init__(self, size=100):
        screen.onkey(self.quit, "q")
        self.size_face = size
        self.size_dot = 10
        self.iticks = 0
        self.isides = 360/60
        self.last = 0
        self.refresh()
        self.tick()

    def draw_dot(self, angle, color, size):
        screen.up();screen.home();screen.color(color, color)
        screen.right(angle * self.isides)
        screen.down();screen.forward(self.size_face)
        screen.dot(size, color)

    def refresh(self):
        screen.up();screen.home()
        screen.circle(self.size_face)
        for deg in range(60):
            self.draw_dot(deg, "gray", self.size_dot)
                
    def draw_tick(self, angle):
        self.draw_dot(self.last, "gray", self.size_dot)
        self.draw_dot(angle, "red", self.size_dot - 1)
        self.last = angle          

    def quit(self):
        screen.ontimer(self.draw_tick, 0) # cancel
        screen.bye()

    def tick(self):
        self.draw_tick(self.iticks)
        self.iticks += 1
        if self.iticks >= 60:
            self.iticks = 0
        screen.ontimer(self.tick, 1000)

screen.ht()
screen.speed(0);screen.delay(0)

demo = Clocker(size=200)
screen.listen()
screen.done()




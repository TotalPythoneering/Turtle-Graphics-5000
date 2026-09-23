# MISSION: Package for the Python 5000 educational opportunity.
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-01 16:01:42
# FILE: Stack.py
# AUTHOR: Randall Nagy
#
import turtle


'''
Save & restore our most often changed values.
'''
class Stack:

    def __init__(self):
        self.hcolor = None
        self.pos    = None
        self.hold   = None
        self.orient = None


    '''
    Save the state
    '''
    def push(self):
        self.hcolor = turtle.color() # save
        self.pos = turtle.pos()      # save
        self.hold = turtle.width()   # save
        self.orient = turtle.heading()


    '''
    Execute a generic, no-parameter, function
    '''
    def execute(self, xpos, ypos, func, keep_pos=False):
        self.push()
        turtle.penup()
        turtle.goto(xpos, ypos)
        turtle.pendown()
        func()
        self.pop(keep_pos)


    '''
    Restore the state - keep_pos to preserve present pos
    '''
    def pop(self, keep_pos=False):
        if(self.hold is None):
            return
        turtle.width(self.hold)
        turtle.color(self.hcolor[0], self.hcolor[1])
        turtle.setheading(self.orient)
        if keep_pos is False:
            turtle.penup()
            turtle.goto(self.pos[0], self.pos[1])
            turtle.pendown()


got_it = False


def say_hello():
    global got_it
    got_it = True


if __name__ == "__main__":
    test = State()
    turtle.goto(100, 100)
    test.execute(0, 0, say_hello)
    if(got_it is False):
        print("error01")
    else:
        pos = turtle.pos()
        if (pos[0] is 100 and pos[1] is 100):
            print("okay")
        else:
            print("error2")





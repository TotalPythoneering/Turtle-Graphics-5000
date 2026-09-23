# MISSION: Package for the Python 5000 educational opportunity.
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-01 16:01:42
# FILE: EnumPoly.py
# AUTHOR: Randall Nagy
#
import turtle
import StateSaver.Stack as Stack

'''
Parameterized Location Generator / Player
'''
class Enumerator(Stack.Stack):

    def __init__(self, sides):
        super().__init__()
        self.sides = sides

    def next(self):
        angle = 360/self.sides
        for ss in range(self.sides):
            ss += 1
            yield round(angle * ss)
        
    def enum(self, func, args):
        super().push()
        for val in self.next():
            func(val, args)
        super().pop(True)

# MISSION: The complete set of examples for ''Python 5000 - Turtle Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-08-09 05:18:34
# FILE: ex_14_screen_mgmt.py
# AUTHOR: Randall Nagy
#
import turtle

# Screen Size
print("1.1",turtle.screensize())
turtle.screensize(800, 600)
print("1.2",turtle.screensize())

# Reset Screen Turtles to original state(s.)
# Homes Origin. Callbacks preserved (etc.)
turtle.goto(120, 210)
turtle.resetscreen()        # same as  turtle.reset()
print("1.3", turtle.pos())
print("1.4",turtle.screensize())

# resetscreen + clears all to default states & colors.
turtle.clearscreen()        # same as turtle.clear()
print("1.5",turtle.screensize())


turtle.done()



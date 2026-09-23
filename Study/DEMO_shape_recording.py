# MISSION: The complete set of examples and source code for ''Python 5000 - Turtle
# Graphics.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-5000
# DATE: 2018-07-21 01:17:18
# FILE: DEMO_shape_recording.py
# AUTHOR: Randall Nagy
# DEMO_shape_recording.py
#
import turtle

def draw_shape(robot):
    robot.penup()
    robot.goto(-200, 0)
    robot.pendown()
    robot.begin_poly()
    robot.pensize("10")
    robot.color("blue")
    for seg in range(10, 100, 5):
        robot.left(45)
        robot.forward(seg)
    robot.end_poly()


draw_shape(turtle)

shape = turtle.Shape("compound")
points = turtle.get_poly()
shape.addcomponent(points, "gold", "green")
turtle.register_shape("MyShape", shape)

turtle.penup()
turtle.shape("MyShape")
turtle.goto(300, 0)
turtle.stamp()


turtle.done()

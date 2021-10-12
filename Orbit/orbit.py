
from turtle import *
import time

planetOne=[1, 0, 55]
planetTwo = [2, 0.5, 30]
planetThree = [3, 2, 25]
planets = [planetOne, planetTwo, planetThree]
distanceScale = 200


screen = Screen()
screen.tracer(0)
turtle = Turtle()
turtle.setheading(90)


def drawplanet(t,p):
    t.forward(p[1] * distanceScale)
    t.pendown()
    t.circle(p[2])
    t.penup()
    t.goto(0, 0)

def planetloop():
    direction=0
    turtle.penup()
    'to be finished'



def draw():
    turtle.clear()
    for planet in planets:
        drawplanet(turtle, planet)

    screen.update()
    turtle.left(1)
    screen.ontimer(draw, 200)  

draw()

screen.mainloop()

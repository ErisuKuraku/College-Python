
from turtle import *

planetOne=[1, 1, 10]
planetTwo = [2, 0.5, 30]
planets = [planetOne, planetTwo]
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



def draw():
    turtle.clear()
    for planet in planets:
        drawplanet(turtle, planet)
    screen.update()
    turtle.left(1)
    screen.ontimer(draw, 200)  

draw()

screen.mainloop()

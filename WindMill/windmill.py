from turtle import Screen, Turtle

file = open('length.txt', 'r')
length = file.read()
length = int(length)

def rectangle(t):
    t.forward(50)
    t.left(90)
    t.backward(5)
    t.pendown()

    for _ in range(2):
        t.forward(10)
        t.right(90)
        t.forward(length)
        t.right(90)

    t.penup()

def windmill(t):
       t.penup()
       rectangle(t)
       t.goto(0, 0)

screen = Screen()
screen.tracer(0)

turtle = Turtle()
turtle.setheading(90)

def rotate():
    turtle.clear()
    windmill(turtle)
    screen.update()
    turtle.left(1)

    screen.ontimer(rotate, 40)  

rotate()

screen.mainloop()

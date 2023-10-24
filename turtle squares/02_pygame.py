import turtle
pen = turtle.Turtle()

screen = turtle.Screen()
screen.listen() 

# movements
def move_left():
    pen.penup()
    pen.setheading(180)
    pen.fd(100)

def move_right():
    pen.penup()
    pen.setheading(0)
    pen.fd(100)

def move_up():
    pen.penup()
    pen.setheading(90)
    pen.fd(100)

def move_down():
    pen.penup()
    pen.setheading(270)
    pen.fd(100)


# triangle
def triangle():
    pen.begin_fill()
    pen.fillcolor("blue")
    pen.pendown()
    for i in range(3):
        pen.lt(120)
        pen.fd(200)
    pen.end_fill()
    pen.penup()

# square
def square():
    pen.begin_fill()
    pen.fillcolor("red")
    pen.pendown()
    for i in range(4):
        pen.fd(150)
        pen.rt(90)
    pen.end_fill()
    pen.penup()

# circle
def circle():
    pen.begin_fill()
    pen.fillcolor("green")
    pen.down()
    pen.circle(100)
    pen.end_fill()
    pen.penup()

# Commands
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.onkey(square, "s")
screen.onkey(triangle, "t")
screen.onkey(circle, "c")

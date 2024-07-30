from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def clear():
    t.clear()
    t.penup()
    t.setposition(0, 0)
    t.setheading(0)
    t.pendown()


def clockwise():
    t.setheading(t.heading() - 10)


def counter_clockwise():
    t.setheading(t.heading() + 10)


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(move_backwards, 's')
screen.onkey(clockwise, 'd')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()

import turtle
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.speed("fastest")
  
  
def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_clockwise():
  tim.left(10)


def move_anticlockwise():
   tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="c", fun=clear)
screen = Screen()
screen.exitonclick()

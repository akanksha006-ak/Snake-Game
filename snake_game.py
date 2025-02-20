# import packages
import turtle
import random 
import time

# creating screen 
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("Green")

# creating border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(688)
turtle.right(98)
turtle.forward(588)
turtle.right(98)
turtle.forward(688)
turtle.right(98)
turtle.forward(588)
turtle.penup()
turtle.hideturtle()
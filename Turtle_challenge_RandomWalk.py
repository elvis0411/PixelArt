from turtle import Screen, Turtle, pencolor
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark olive green")


screen = Screen()
screen.colormode(255)
width = 1
directions = [0,90,180,270,360]
for i in range(500):
    timmy_the_turtle.pendown()
    timmy_the_turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    timmy_the_turtle.width(10)
    timmy_the_turtle.speed(0)
    timmy_the_turtle.forward(20)
    timmy_the_turtle.setheading(random.choice(directions))
    width +=0.5



screen.exitonclick()
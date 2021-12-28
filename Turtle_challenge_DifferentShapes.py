from turtle import Screen, Turtle, pencolor
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark olive green")

number_sides = [3,4,5,6,7,8,9,10]
screen = Screen()
screen.colormode(255)

for i in number_sides:
    timmy_the_turtle.pendown()
    timmy_the_turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for _ in range(i):        
        corner_angle = 360/i
        timmy_the_turtle.right(corner_angle)
        timmy_the_turtle.forward(100)



screen.exitonclick()
from turtle import Screen, Turtle, pencolor
import random

def color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark olive green")

screen = Screen()
screen.colormode(255)

number_cicles = 50
cicles_radius = 200
timmy_the_turtle.speed(0)
timmy_the_turtle.width(1)
current_heading = 0

for i in range(360):
    timmy_the_turtle.pendown()
    timmy_the_turtle.color(color())
    timmy_the_turtle.setheading(current_heading)
    timmy_the_turtle.circle(cicles_radius)
    current_heading += 5

screen.exitonclick()
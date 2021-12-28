from turtle import Screen, Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark olive green")

step = 0
dash_size = 5
for _ in range(50):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(dash_size)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(dash_size)
    step +=1

screen = Screen()
screen.exitonclick()
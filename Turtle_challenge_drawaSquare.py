from turtle import Screen, Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark olive green")

position = [[100, 0],[ 100,100],[0,100], [0,0]]

for points in position:
    timmy_the_turtle.pendown()
    timmy_the_turtle.setpos(points)

screen = Screen()
screen.exitonclick()

#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    
#    rgb_colors.append((r,g,b))
#
#print(rgb_colors)
from turtle import Screen, Turtle, pencolor
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("dark olive green")
timmy_the_turtle.penup()
timmy_the_turtle.speed(0)


screen = Screen()
screen.colormode(255)

dot_radius = 20
space_size = 50
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49),
              (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71),
              (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158),
              (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), 
              (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), 
              (176,192, 209)]

def dot_color():
    color = random.choice(color_list)
    return color

lines = -300
for i in range(10):
    timmy_the_turtle.hideturtle()
    timmy_the_turtle.setx(-400)
    timmy_the_turtle.sety(lines)
    timmy_the_turtle.showturtle()
    for j in range(9):
        timmy_the_turtle.dot(dot_radius,dot_color())
        timmy_the_turtle.forward(dot_radius*2+space_size)    
    timmy_the_turtle.dot(dot_radius,dot_color())
    lines = lines + dot_radius+space_size
timmy_the_turtle.hideturtle()
screen.exitonclick()

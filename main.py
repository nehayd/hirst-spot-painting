import colorgram

# To get the colours in an image
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
colour_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 
62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 
59), (53, 70, 64)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.pendown()
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(colour_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.setheading(180)
        tim.penup()
        tim.forward(500)
        tim.pendown()
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
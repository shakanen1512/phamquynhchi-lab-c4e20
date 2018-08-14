from turtle import *

speed(-1)
shape("turtle")

def draw_square(length, square_color):
    color(square_color)
    left(90)
    forward(length)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
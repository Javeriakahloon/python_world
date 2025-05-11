import turtle
import colorsys

s = turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.speed(0)
n = 70
h = 0

turtle.colormode(1)  # RGB values between 0–1

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)

turtle.done()

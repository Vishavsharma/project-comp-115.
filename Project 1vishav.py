import turtle
import math

def draw_mandala(radius, num_petals):
    angle = 360 / num_petals

    for _ in range(num_petals):
        draw_petal(radius)
        turtle.right(angle)

def draw_petal(radius):
    turtle.color("blue")  # You can change the color as desired
    turtle.fillcolor("purple")  # You can change the fill color as desired
    turtle.begin_fill()

    for _ in range(2):
        draw_half_petal(radius)
        turtle.left(180)

    turtle.end_fill()

def draw_half_petal(radius):
    angle = 60
    side_length = 2 * radius * math.sin(math.radians(angle / 2))

    turtle.forward(radius)
    turtle.left(angle / 2)
    turtle.forward(side_length)
    turtle.left(angle / 2)
    turtle.forward(radius)

def main():
    turtle.speed(2)  # Adjust the speed as needed
    turtle.bgcolor("white")  # Background color

    radius = int(turtle.numinput("Mandala Parameters", "Enter the radius of the petal:", default=100, minval=50, maxval=200))
    num_petals = int(turtle.numinput("Mandala Parameters", "Enter the number of petals:", default=12, minval=4, maxval=36))

    draw_mandala(radius, num_petals)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

import turtle
def draw_pentagon():
    turtle.color("blue")
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)
    turtle.done()
draw_pentagon()
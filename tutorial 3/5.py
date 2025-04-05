import turtle
def draw_radial_hexagons():
    def hexagon():
        for _ in range(6):
            turtle.forward(50)
            turtle.right(60)
    turtle.speed(0)
    for _ in range(10):
        hexagon()
        turtle.right(36)
    turtle.done()
draw_radial_hexagons()
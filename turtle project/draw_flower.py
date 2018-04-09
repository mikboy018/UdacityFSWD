import turtle as pencil

def draw_flower():
    counter = 0
    window = pencil.Screen()
    window.bgcolor("blue")
    
    marker = pencil.Turtle()
    marker.color("white")
    marker.speed(22)
    while counter < 36:
        draw_petal(marker)
        marker.right(10)
        counter+=1
    marker.home()
    marker.right(90)
    marker.forward(200)


def draw_petal(marker):
    counter = 0
    marker.right(25)
    marker.forward(50)
    marker.left(50)
    marker.forward(50)
    marker.right(155)
    marker.forward(50)
    marker.right(25)
    marker.forward(50)

draw_flower()

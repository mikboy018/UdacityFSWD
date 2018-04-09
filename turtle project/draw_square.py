import turtle as pencil

def draw_shapes():
    counter = 0
    window = pencil.Screen()
    window.bgcolor("blue")

    #draws a square
    marker = pencil.Turtle()
    marker.shape("turtle")
    marker.color("yellow")
    marker.speed(2)
    while counter < 36:
        draw_square(marker)
        marker.right(10)
        counter +=1
        
    #draws a circle
    circ = pencil.Turtle()
    circ.circle(100)

    #draws a triangle
    tri = pencil.Turtle()
    tri.color("white")
    counter = 0
    while counter < 3:
        tri.forward(100)
        tri.right(120)
        counter += 1

def draw_square(marker):
    marker.shape("turtle")
    marker.color("white")
    counter = 0
    
    while counter < 4:
        marker.forward(100)
        marker.right(90)
        counter+=1
    

draw_shapes()

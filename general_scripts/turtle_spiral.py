import turtle

wn = turtle.Screen()
wn.screensize(500,500)
wn.bgcolor("lightgreen")
wn.title("Turtle Spiral")

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("blue")

steve.penup()
size = 20

for i in range(60):
    steve.stamp()
    size = size + 3
    steve.forward(size)
    steve.right(24)

wn.mainloop()


import turtle

wn = turtle.Screen()
wn.setup(600,600)
wn.bgcolor("lightgreen")
wn.title("Turtle clock")
 
steve = turtle.Turtle()
steve.shape("turtle")
steve.color("blue")

steve.penup()

# This is how far the turtle moves whilst creating one line

for i in range(12):
    steve.forward(200)
    steve.pendown()
    steve.forward(20)
    steve.penup()
    steve.forward(20)
    steve.stamp()
    steve.backward(240)
    steve.right(30)

wn.mainloop()

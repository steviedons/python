import turtle

wn = turtle.Screen()
wn.setup(500, 500)
wn.bgcolor("lightblue")
wn.title("Drunk Turtle")

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("red")

heading = 0

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    steve.forward(50)
    steve.left(i)
    steve.forward(50)
    heading = heading + i

print("The pirates heading was:" + str(heading))
wn.mainloop()

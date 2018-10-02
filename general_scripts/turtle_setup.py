import turtle

def make_window(colr, title):
    """
    Set up the window with the given background color and title.  Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(title)
    return w

def make_turtle(colr, sz):
    """
    Set up a turle with a given color and pensize.  Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

def draw_rectangle(t, w, h):
    """
    Get turtle t to draw a rectangle of width w and height h.i
    """
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz):
    """ 
    Create a square with turtle tx and size sz. This function calls the draw_rectangle() 
    """
    draw_rectangle(tx,sz,sz)

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)

wn = make_window("lightgreen", "Steve and Jack dancing")
steve = make_turtle("hotpink", 5)
jack = make_turtle("black", 2)

# Exercise 4.9 1
#for i in range(5):
#    steve.pendown()
#    draw_square(steve,50)
#    steve.penup()
#    steve.forward(100)

# Exercise 4.9 1
#for i in range(1,7):
#    steve.pendown()
#    draw_square(steve,(40*i*2))
#    steve.penup()
#    steve.right(90)
#    steve.forward(40)
#    steve.right(90)
#    steve.forward(40)
#    steve.left(180)

draw_poly(steve, 8, 50)

wn.mainloop()


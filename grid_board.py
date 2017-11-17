import turtle

wn=turtle.Screen()
wn.bgcolor('blue')
wn.title('gridboard')

greg=turtle.Turtle()
greg.speed(0)

def square(size, alternate, color):
    greg.color(color)
    greg.begin_fill()
    for i in range(8):
        greg.fd(size)
        greg.lt(90)
    greg.end_fill()
    greg.fd(size)

def row(size, alternate, color1, color2):
    for i in range(8):
     if (True == alternate):
        square(size, alternate, color1)
        square(size, alternate, color2)
    else:
        square(size, alternate, color2)
        square(size, alternate, color1)

def gridboard(size,alternate,color1,color2):
    greg.pu()
    greg.goto(-(size*4),(size*4))
    for i in range(8):
        row(size,alternate,color1,color2)
        greg.bk(size*8)
        greg.rt(90)
        greg.fd(size)
        greg.lt(90)
        if (alternate==True) :
            alternate=False
        else:
            alternate=True

gridboard(50, True, 'red', 'yellow')
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

def Rechtecke():
    t = turtle.Pen()
    t.speed(1)
    t.color("orange")
    width = 200
    height = 100
    flag = 0
    for r in range(0,2):
        for index in range(0, 4):
            if flag == 0:
                t.forward(width)
                flag = 1
            else:
                t.forward(height)
                flag = 0
            t.right(90)
        t.penup()
        t.goto(height/2,-(width/4))
        height = 25
        width = 50
        t.pendown()
    t.goto(0,0)

def Herz():
    t = turtle.Pen()
    t.speed(1)
    t.color("orange")
    t.color("red")
    rd_cerc = 80
    t.right(90)
    t.circle(rd_cerc,-180)
    t.right(180)
    t.circle(rd_cerc,-180)
    t.goto(2*rd_cerc,-200)
    t.goto(0,0)


def dreptunghi_casa():
    pass

def Hauser():
    c1 = turtle.Pen()
    c1.color("yellow")

    c2 = turtle.Pen()
    c2.color("pink")

    c1.speed(5)
    c2.speed(5)

    c1.penup()
    c2.penup()

    c1.goto(-100,0)
    c1.pendown()

    c2.goto(100,0)
    c2.pendown()
    c1.forward(100)
    c2.forward(100)

    c1.left(90)
    c2.left(90)

    c1.forward(75)
    c2.forward(75)

    c1.left(90)
    c2.left(90)

    c1.forward(100)
    c2.forward(100)

    c1.left(90)
    c2.left(90)

    c1.forward(75)
    c2.forward(75)

    #c1.penup()
    c2.penup()

    #c1.goto(-50,300)
    c2.goto(150,30)

    c1.pendown()
    c2.pendown()



#Rechtecke()
#Herz()
Hauser()
turtle.done()
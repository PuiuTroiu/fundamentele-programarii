# import turtle
# import sys
# def cmdW(pen2):
#     pen2.forward(10)
#
# def cmdS(pen2):
#     pen2.forward(-10)
#
# def cmdD(pen2):
#     pen2.right(45)
#
# def cmdA(pen2):
#     pen2.left(45)
#
# def cmdF(pen2):
#     pen2.penup()
#
# def cmdG(pen2):
#     pen2.pendown()
#
# def cmdExist():
#     sys.exit()
#
# def cmdAll():
#     pen2 = turtle.Pen()
#     pen2.color("red")
#     turtle.onkey(cmdW(pen2), 'w')
#     turtle.onkey(cmdA(pen2), 'a')
#     turtle.onkey(cmdS(pen2), 's')
#     turtle.onkey(cmdD(pen2), 'd')
#     turtle.onkey(cmdF(pen2), 'f')
#     turtle.onkey(cmdG(pen2), 'g')
#     turtle.listen()
#     turtle.done()
#
# # Menține fereastra deschisă și ascultă evenimentele tastaturii
#

import turtle
import sys


def cmdW(pen2):
    f = open('./cmd.txt', 'a')

    pen2.forward(10)
    f.write('W')

def cmdS(pen2):
    f = open('./cmd.txt', 'a')

    pen2.forward(-10)
    f.write('S')


def cmdD(pen2):
    f = open('./cmd.txt', 'a')

    pen2.right(45)
    f.write('D')

def cmdA(pen2):
    f = open('./cmd.txt', 'a')

    pen2.left(45)
    f.write('A')

def cmdF(pen2):
    f = open('./cmd.txt', 'a')

    pen2.penup()
    f.write('F')


def cmdG(pen2):
    f = open('./cmd.txt', 'a')

    pen2.pendown()
    f.write('G')


def cmdExist():
    turtle.bye()

def cmdAll(screen):
    f = open('./cmd.txt', 'a')

    pen2 = turtle.Pen()
    pen2.color("red")
    turtle.onkey(lambda: cmdW(pen2), 'w')
    turtle.onkey(lambda: cmdA(pen2), 'a')
    turtle.onkey(lambda: cmdS(pen2), 's')
    turtle.onkey(lambda: cmdD(pen2), 'd')
    turtle.onkey(lambda: cmdF(pen2), 'f')
    turtle.onkey(lambda: cmdG(pen2), 'g')
    turtle.onkey(cmdExist, 'q')  # Adăugat pentru a ieși din program cu 'q'
    turtle.listen()
    f.write('\n')
    turtle.done()


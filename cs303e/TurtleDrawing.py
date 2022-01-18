# File: GermanFlag.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 11/29/2020
# Date Last Modified: 11/30/2020
# Description of the Program: This program use python to draw a German flag.

import turtle

#create a function to draw a rectangle
def drawFlag (ttl, x, y, length, width, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.color(color)
    for count in range (4):
        ttl.begin_fill()
        ttl.forward(length)
        ttl.right(90)
        ttl.forward(width)
        ttl.right(90)
        ttl.end_fill()
        ttl.hideturtle()
    ttl.penup()

#black rectangle
flagBlack = turtle.Turtle()
flagBlack.speed (10)
drawFlag(flagBlack, -250, 150, 500, 100, "black")

#red rectangle
flagRed = turtle.Turtle()
flagRed.speed (10)
drawFlag(flagRed, -250, 50, 500, 100, "red")

#gold rectangle
flagYellow = turtle.Turtle()
flagYellow.speed (10)
drawFlag(flagYellow, -250, -50, 500, 100, "gold")

#make the picture stay
turtle.done()



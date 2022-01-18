# File: Project3.py
# Student: Enya Liu
# UT EID: el27773
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 12/3/2020
# Date Last Modified: 12/4/2020
# Description of Program: This program use turtle to draw an American flag.

import turtle

# create a function to draw a rectangle
def drawFlag(ttl, x, y, length, width, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.color(color)
    for count in range(2):
        ttl.begin_fill()
        ttl.forward(length)
        ttl.right(90)
        ttl.forward(width)
        ttl.right(90)
        ttl.end_fill()
        ttl.hideturtle()
    ttl.penup()


def drawWhiteStar(ttl, x, y):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.color('white')
    for i in range (5):
        ttl.begin_fill()
        ttl.left(18)
        ttl.forward(20)
        ttl.left(162)
        ttl.forward(10)
        ttl.right(72)
        ttl.forward(10)
        ttl.left(162)
        ttl.forward(20)
        ttl.right(198)
        ttl.end_fill()
        ttl.hideturtle()
    ttl.penup()

#colors
myBlue = (0, 32, 91)
myRed = (191, 13, 62)

# draw the flag's background
ypoint = 250
for i in range(14):
    if i == 1 or i % 2 == 1:
        # white stripe
        whiteStripe = turtle.Turtle()
        whiteStripe.speed(10)
        drawFlag(whiteStripe, -475, ypoint, 950, 38, "white")
        ypoint -= 38
    else:
        # red stripe
        redStripe = turtle.Turtle()
        redStripe.screen.colormode(255)
        redStripe.speed(10)
        drawFlag(redStripe, -475, ypoint, 950, 38, myRed)
        ypoint -= 38

# draw the blue rectangle on the top left corner
blueRect = turtle.Turtle()
blueRect.screen.colormode(255)
blueRect.speed(10)
drawFlag(blueRect, -475, 250, 380, 266, myBlue)

#draw white stars on the top left
count = 0
xlab = -444
ylab = 222
for j in range (4):
    for i in range (11):
        if i == 0 or i % 2 == 0:
            whiteStar = turtle.Turtle()
            whiteStar.speed(10)
            drawWhiteStar(whiteStar, xlab, ylab)
            xlab = xlab + 31
            count += 1
            ylab = ylab - 27
            if count == 11:
                xlab = -444
                ylab = ylab - 27
                count = 0
        else:
            whiteStar = turtle.Turtle()
            whiteStar.speed(10)
            drawWhiteStar(whiteStar, xlab, ylab)
            xlab = xlab + 31
            ylab = ylab + 27
            count += 1
            if count == 11:
                xlab = -444
                ylab = ylab - 54
                count = 0

#add the last line of stars
for lastline in range (6):
    whiteStar = turtle.Turtle()
    whiteStar.speed(10)
    drawWhiteStar(whiteStar, xlab, 10)
    xlab = xlab + 62

turtle.done()

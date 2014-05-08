__author__ = 'Irrevocable Cascade & interactivepython.org'

import turtle
import random

def list_sum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + list_sum(numList[1:])


def factorial(number):
    if number <= 1:
        return number
    else:
        return number * factorial(number - 1)

def to_string(n, base):
    convs="0123456789ABCDEF"
    if n < base:
        return convs[n]
    else:
        return to_string(n // base, base) + convs[n % base]


def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    r = reverse_string(s)
    return r == s


def draw_spiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.color()
        myTurtle.forward(lineLen)
        myTurtle.right(32)
        myTurtle.forward(3)
        myTurtle.left(10)
        draw_spiral(myTurtle, lineLen - 5)

def tree(branchLen, t):
    if branchLen > 5:
        if branchLen >= 150:
            t.color("brown")
            t.width(20)
        if 150 > branchLen > 60:
            t.color("green")
            t.width(15)
        if branchLen < 60:
            t.color("yellow")
            t.width(10)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 30, t)
        t.left(40)
        tree(branchLen - 30, t)
        t.right(20)
        t.penup()
        t.backward(branchLen)
        t.pendown()

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(155, t)
    t.left(90)
    t.color("green")
    t.forward(300)
    t.backward(300)
    t.right(180)
    t.forward(300)
    myWin.exitonclick()

main()


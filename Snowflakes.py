import turtle
import random
elsa = turtle.Turtle()
elsa.speed(0)

#set background in grey
turtle.Screen().bgcolor("grey")

#create a list of colours
colours = ["cyan", "purple", "white", "blue", "yellow", "orange", "red", "pink", "green"]

#move the pen in starting position
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

#create one branch of the snowflake by using for-loops:
def branch():
   for a in range(3):
        for b in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
   elsa.right(90)
   elsa.forward(90)

#create one branch of the snowflake by using while-loops:

def whilebranch():
    y = 0
    while (y < 3):
        x = 0
        while(x < 3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
            x += 1
        x = 0
        while(x < 1):
            elsa.left(90)
            elsa.backward(30)
            elsa.left(45)
            x += 1
        y += 1
    elsa.right(90)
    elsa.forward(90)

#draw branch 8 times with for-loop:
def draw_forloop():
    for i in range(8):
        branch()
        elsa.color(random.choice(colours))
        elsa.left(45)

#draw branch 8 times with while-loop:
def draw_whileloop():
    x = 0
    while(x < 8):
        whilebranch()
        elsa.color(random.choice(colours))
        elsa.left(45)
        x += 1

draw_whileloop()

turtle.Screen().exitonclick()
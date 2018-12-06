from turtle import *
from random import randint

speed(10)
penup()
goto(-140, 140)

for step in range(21):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)    
    
coding = Turtle()
coding.color('red')
coding.shape('turtle')
    
coding.penup()
coding.goto(-160, 100)
coding.pendown()

documentary = Turtle()
documentary.color('green')
documentary.shape('turtle')
    
documentary.penup()
documentary.goto(-160, 70)
documentary.pendown()

trading = Turtle()
trading.color('blue')
trading.shape('turtle')
    
trading.penup()
trading.goto(-160, 40)
trading.pendown()

photography = Turtle()
photography.color('yellow')
photography.shape('turtle')
    
photography.penup()
photography.goto(-160, 10)
photography.pendown()

for turn in range(100):
    coding.forward(randint(1,8))
    documentary.forward(randint(1,8))
    trading.forward(randint(1,8))
    photography.forward(randint(1,8))
    trading.right(1)

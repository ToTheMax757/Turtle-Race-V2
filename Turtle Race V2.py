from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

pinky = Turtle()
pinky.color('magenta')
pinky.shape('turtle')

pinky.penup()
pinky.goto(-160, 100)
pinky.pendown()

for turn in range(10):
  pinky.right(36)

lima = Turtle()
lima.color('lime')
lima.shape('turtle')

lima.penup()
lima.goto(-160, 70)
lima.pendown()

for turn in range(72):
  lima.left(5)

piper = Turtle()
piper.shape('turtle')
piper.color('cyan')

piper.penup()
piper.goto(-160, 40)
piper.pendown()

for turn in range(60):
  piper.right(6)

Nugget = Turtle()
Nugget.shape('turtle')
Nugget.color('orange')

Nugget.penup()
Nugget.goto(-160, 10)
Nugget.pendown()

for turn in range(30):
  Nugget.left(12)

for turn in range(100):
  pinky.forward(randint(1,5))
  lima.forward(randint(1,5))
  piper.forward(randint(1,5))
  Nugget.forward(randint(1,5))
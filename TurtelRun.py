from turtle import *
from random import randint

speed(10) #скорость движения
penup() #поднять перо
goto(-140, 140) #передвижение черепашки на старт

for step in range(15):
    write(step, align='center') #вывести число
    right(90) #повернуть направо на 90 градусов
    forward(10) #отойти от числа на 10 шагов
    for line in range(15):
        pendown()
        forward(5)
        penup()
        forward(5)
    backward(160) #идти назад 160 шагов
    left(90)
    forward(20)

#Добавление и настройка черепашек
ada = Turtle()
ada.color('red')
ada.shape('turtle')

tom = Turtle()
tom.color('blue')
tom.shape('turtle')

bob = Turtle()
bob.color('green')
bob.shape('turtle')

lok = Turtle()
lok.color('yellow')
lok.shape('turtle')

tok = Turtle()
tok.color('purple')
tok.shape('turtle')

#Перемещение черепашек к началу гонки
ada.penup()
ada.goto(-160,110)
ada.right(360) #Анимация вокруг себя
ada.pendown()

tom.penup()
tom.goto(-160,80)
for turn in range(2):
    tom.left(15)
    tom.right(30)
    tom.left(15)
tom.pendown()

bob.penup()
bob.goto(-160,50)
for turn in range(2):
    bob.right(45)
    bob.left(90)
    bob.right(45)
bob.pendown()

lok.penup()
lok.goto(-160,20)
lok.right(360)
lok.pendown()

tok.penup()
tok.goto(-160,-10)
for turn in range(4):
    tok.left(15)
    tok.right(30)
    tok.left(15)
tok.pendown()

#Перемещение черепашек

for move in range(100):
    ada.forward(randint(1,5))
    tom.forward(randint(1,5))
    bob.forward(randint(1,5))
    lok.forward(randint(1,5))
    tok.forward(randint(1,5))

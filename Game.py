# Turtle-Race game with turtle module.
# Done by Sri Manikanta Palakollu.
# Version - 3.7.0

from turtle import *
from random import randint
import turtle

screen = Screen() # Creates the Screen.
screen.title('Turtle Race by @Sri_Programmer')	
screen.bgcolor('#000000') 
speed(10)	# Game Speed.
penup()
goto(-140,140)

for i in range(15):
	pencolor('white')
	write(i, align = 'center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

def game_exit():
	exit(0)

screen.listen()
screen.onkeypress(game_exit,'q')

ada = Turtle()
ada.color('#e15f41')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('skyblue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

sun = Turtle()
sun.color('#f53b57')
sun.shape('turtle')
sun.penup()
sun.goto(-160,40)
sun.pendown()

moon = Turtle()
moon.color('#4DAF7C')
moon.shape('turtle')
moon.penup()
moon.goto(-160,10)
moon.pendown()

while True:
	
	for turn in range(100):
		ada.forward(randint(1,5))
		bob.forward(randint(1,5))
		sun.forward(randint(1,5))
		moon.forward(randint(1,5))

	"""	if(ada_score >= 100):
			write('Winner is Red', align='right')
			break
		if(bob_score >= 100):
			write('Winner is blue', align='right')
			break
		if(sun_score >= 100):
			write('Winner is skyblue', align='right')
			break
		if(moon_score >= 100):
			write('Winner is silver', align='right')
			break
	"""

from turtle import *
from random import randint
import turtle


#write('Turtle Race', align='up')
#turtle.Screen('Turtle Race')
turtle.color('green')
speed(10)
penup()
goto(-140,140)

for i in range(15):
	write(i, align = 'center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)


ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

#for turn in range(150):
#	ada.forward(randint(1,5))

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

sun = Turtle()
sun.color('skyblue')
sun.shape('turtle')
sun.penup()
sun.goto(-160,40)
sun.pendown()

moon = Turtle()
moon.color('silver')
moon.shape('turtle')
moon.penup()
moon.goto(-160,10)
moon.pendown()
ada_score = 0
bob_score = 0
sun_score = 0
moon_score = 0
for turn in range(100):
	temp = randint(1,5)
	ada.forward(temp)
	ada_score += temp
	temp = randint(1,5)
	bob.forward(temp)
	bob_score += temp
	temp = randint(1,5)
	sun.forward(temp)
	sun_score += temp
	temp = randint(1,5)
	moon.forward(temp)
	moon_score += temp

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






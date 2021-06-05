import turtle
import math
# test

def turtleLetter(letter,tur):
	if letter=="box":
		tur.setheading(0)
		tur.forward(40)
		tur.right(90)
		tur.forward(60)
		tur.right(90)
		tur.forward(40)
		tur.right(90)
		tur.forward(60)

	elif letter == "A":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.fd(30)
		tur.right(180)
		tur.fd(30)
		tur.right(90)
		tur.fd(20)
		tur.right(90)
		tur.fd(30)
		tur.right(180)
		tur.fd(15)
		tur.left(90)
		tur.fd(20)
		tur.pu()
		#fixes
		tur.right(90)
		tur.fd(20)
		tur.right(90)
		tur.fd(35)
		#tur.right(180)
	elif letter == "B":
		pass
	elif letter == "C":
		tur.setheading(0)
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.circle(50,180)
		tur.pu()
	elif letter == "D":
		pass
	elif letter == "E":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.fd(30)
		tur.right(180)
		tur.fd(30)
		tur.right(90)
		tur.fd(20)
		tur.pu()
		tur.right(180)
		tur.fd(20)
		tur.left(90)
		tur.fd(15)
		tur.left(90)
		tur.pd()
		tur.fd(20)
		tur.pu()
		tur.right(180)
		tur.fd(20)
		tur.left(90)
		tur.fd(15)
		tur.left(90)
		tur.pd()
		tur.fd(20)
		tur.pu()
		tur.right(180)
		tur.fd(20)
		#fixes
		tur.right(90)
		tur.fd(35)
		tur.right(90)
		tur.fd(35)
		#tur.right(180)'''
	elif letter == "F":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.fd(30)
		tur.right(180)
		tur.fd(30)
		tur.right(90)
		tur.fd(20)
		tur.pu()
		tur.right(180)
		tur.fd(20)
		tur.left(90)
		tur.fd(15)
		tur.left(90)
		tur.pd()
		tur.fd(20)
		tur.pu()
		tur.right(180)
		tur.fd(20)
		# fixes
		tur.right(90)
		tur.fd(20)
		tur.right(90)
		tur.fd(35)
	# tur.right(180)'''
	elif letter == "G":
		tur.setheading(0)
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.circle(50,270)
		tur.left(20)
		tur.pu()
	elif letter == "H":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.fd(30)
		tur.right(180)
		tur.fd(15)
		tur.right(90)
		tur.fd(20)
		tur.left(90)
		tur.fd(15)
		tur.right(180)
		tur.fd(30)
		tur.pu()
		tur.right(180)
		tur.fd(15)
		tur.left(90)
		tur.fd(20)
		tur.left(90)
		tur.fd(15)
		# fixes
		tur.right(180)
		tur.fd(35)
		tur.right(90)
		tur.fd(35)
	# tur.right(180)'''
	elif letter == "I":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.right(90)
  	  	tur.forward(WIDTH)
    		tur.backward(WIDTH / 2)
    		tur.left(90)
    		tur.forward(HEIGHT)
    		tur.right(90)
    		tur.backward(WIDTH / 2)
    		tur.forward(WIDTH)
	elif letter == "J":
		pass
	elif letter == "K":
		pass
	elif letter == "L":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.forward(50)
		tur.back(50)
		tur.right(90)
		tur.forward(40)
		tur.penup()
		tur.forward(10)
	elif letter == "M":
		pass
	elif letter == "N":
		pass
	elif letter == "O":
		pass
	elif letter == "P":
		pass
	elif letter == "Q":
		pass
	elif letter == "R":
		pass
	elif letter == "S":
		pass
	elif letter == "T":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		t.forward (50)
		tur.goto (25, 0)
		tur.right (90)
		tur.forward (100)
	elif letter == "U":
		pass
	elif letter == "V":
		pass
	elif letter == "W":
		pass
	elif letter == "X":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.left(45)
		tur.fd(math.sqrt(1800))
		tur.left(180)
		tur.fd(math.sqrt(1800))
		tur.pu()
		tur.right(135)
		tur.fd(30)
		tur.pd()
		tur.right(135)
		tur.fd(math.sqrt(1800))
		tur.pu()
		# fixes
		tur.right(135)
		tur.fd(35)
		tur.right(90)
		tur.fd(35)
	elif letter == "Y":
		tur.setheading(0)
		tur.pu()
		tur.fd(5)
		tur.right(90)
		tur.fd(5)
		tur.pd()
		tur.left(45)
		tur.fd((math.sqrt(1800)/2))
		tur.left(180)
		tur.fd((math.sqrt(1800))/2)
		tur.pu()
		tur.right(135)
		tur.fd(30)
		tur.pd()
		tur.right(135)
		tur.fd((math.sqrt(1800))/2)
		tur.left(45)
		tur.fd(15)
		tur.pu()
		tur.right(90)
		tur.fd(15)
		#fixes
		tur.right(90)
		tur.fd(35)
		tur.right(90)
		tur.fd(35)
	elif letter == "Z":
		pass


	elif letter == "Ax":
		# code here
		tur.forward(40)

	else:
		#handles space, punctuation, and anything else
		tur.forward(40)

if __name__ == "__main__":
	window = turtle.Screen()
	tur = turtle.Turtle()
	tur.speed(1)
	#turtleLetter("box",tur)
	turtleLetter("A", tur)
	turtleLetter("E", tur)
	turtleLetter("F", tur)
	turtleLetter("H", tur)
	turtleLetter("Y", tur)
	turtleLetter("X", tur)

	window.exitonclick()

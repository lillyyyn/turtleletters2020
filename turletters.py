import turtle, math
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
		pass
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
		pass
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
		pass
	elif letter == "J":
		pass
	elif letter == "K":
		pass
	elif letter == "L":
		pass
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
		pass
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
		tur.rightFi(135)
		tur.fd(35)
		tur.right(90)
		tur.fd(35)
	elif letter == "Y":
		pass
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
	turtleLetter("X", tur)
	turtleLetter("A", tur)
	turtleLetter("E", tur)
	turtleLetter("F", tur)
	turtleLetter("H", tur)

	window.exitonclick()

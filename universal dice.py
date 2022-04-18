a = 0

def hiren():
	import random
	global a
	a = random.randint(1,6)
def play2():
	k = 5

	first = input("Enter First player name:  ")
	second = input("Enter Second player name:  ")

	print("First turn", first,"...are you ready for roll a dice ??",end=" ")
	input("")
	while k <= 8:	
		print(" ")
		hiren()
		print(first,":",a)
		print("Next turn ", second,end=" ")
		input("")

		print(" ")

		hiren()
		print(second,":",a)
		print("Next turn ", first,end=" ")
		input("")

def play4():
	k = 5

	first = input("Enter First player name:  ")
	second = input("Enter Second player name:  ")
	third = input("Enter third player name:  ")
	four = input("Enter fourth player name:  ")

	print(" ")
	print("First turn", first,"...are you ready for roll a dice ??",end=" ")
	input(" ")

	while k <= 8:
		print(" ")
		hiren()
		print(first,":",a)
		print("Next turn ", second,end=" ")
		input("")

		print(" ")

		hiren()
		print(second,":",a)
		print("Next turn ", third,end=" ")
		input("")

		print(" ")

		hiren()
		print(third,":",a)
		print("Next turn ", four,end=" ")
		input("")

		print(" ")

		hiren()
		print(four,":",a)
		print("Next turn ", first,end=" ")
		input("")


def play1():
	k = 5
	while k <= 8:	
		print(" ")
		hiren()
		print(a)
		input("roll another ??")



def play3():
	k = 5

	first = input("Enter First player name:  ")
	second = input("Enter Second player name:  ")
	third = input("Enter third player name:  ")

	print(" ")
	print("First turn ", first,"are you ready for roll a dice ??",end=" ")
	input(" ")

	while k <= 8:
		print(" ")
		hiren()
		print(first,":",a)
		print("Next turn ", second,end=" ")
		input("")

		print(" ")

		hiren()
		print(second,":",a)
		print("Next turn ", third,end=" ")
		input("")

		print(" ")


		hiren()
		print(third,":",a)
		print("Next turn ", first,end=" ")
		input("")

def all():
	play = int(input("Enter number of players: "))
	print("")
	
	print("")

	if play==1:
		print("nice")
		play1()
	elif play==2:
		print("nice")
		play2()
	elif play==3:
		print("nice")
		play3()
	elif play==4:
		print("nice")
		play4()
	else:
		print("maximum 4 player allowed")
		print(" ")
		all()

all()
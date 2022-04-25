a = int(input("Enter a number of players "))
b = []
for j in range(a):
	k = input("Enter a name of player ")
	b.append(k)

lenth = len(b)
import random

while 8<9:
	for ka in range(lenth):
		print("turn is" ,b[ka])
		print(random.randint(1,6))
		input()

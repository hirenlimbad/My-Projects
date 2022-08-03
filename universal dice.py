import random

a = int(input("Enter a number of players "))
b = []
for j in range(1,a+1):
    f ="Enter a name of player "+ str(j)
    k = input(f)
    b.append(k)

lenth = len(b)

jb = 0
print('note: for exit type anything and hit enter')
while jb != 5:
    for ka in range(lenth):
        print("turn is " + b[ka],end=' ')
        print(random.randint(1,6))
        t = input()
        
    if t != '':
        jb = 5

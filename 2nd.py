a = int(input("Enter a number of list element: "))
b = []

for c in range(a):
	f = int(input("Enter a number for list "))
	b.append(f)

t = 0
for hiren in b:
	t = t+hiren

print(t)
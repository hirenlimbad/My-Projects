a = int(input("Enter a number of list element: "))
b = []


for c in range(a):
	f = int(input("Enter a number for list "))
	b.append(f)

mini,high = min(b),max(b)

print("Minimum value in list is: ",mini)
print("Maximum value in list is: ",high)
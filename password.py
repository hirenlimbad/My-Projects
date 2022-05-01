import string as k
a = k.ascii_lowercase
b = k.ascii_uppercase

g = ['1','2','3','4','5','6','7','8','9','0']
q = [] #lowercase
s =[] #uppercase
spacial = [" ","!","'",'"',"#","$","%","&","(",")","*","+","-",",",".","/",";",":","<",">","=","@","{","}","|","^","~"]
flag = 0


for t in a:
	q.append(t)
for w in b:
	s.append(w)

pass2 = input("Enter your password: ")

for v in pass2:
	if v in g:
		flag=flag+1
		break

for vv in pass2:
	if vv in q:
		flag=flag+1
		break

for v in pass2:
	if v in s:
		flag=flag+1
		break

for v in pass2:
	if v in spacial:
		flag=flag+1
		break
d = len(pass2)
if d > 8:
	flag = flag+1
if d > 16:
	print(" ")
	print("Warning")
	print("your password is too big ")


print(" ")
if flag == 1:
	print("Password strength is too weak")
if flag == 2:
	print("Password strength is weak")
if flag == 3:
	print("Password strength is good")
if flag == 4:
	print("Password strength is very good")
if flag == 5:
	print("Password strength is an excellent")
print("Password rank out of 5: ",flag)
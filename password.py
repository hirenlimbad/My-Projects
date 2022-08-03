flag = 0
#you must have to install python packages.
#for install type in terminal
#pip install packege-name
import string as k
import maskpass as y
import random as ttt
import time as bt

a = k.ascii_lowercase
b = k.ascii_uppercase

g = ['1','2','3','4','5','6','7','8','9','0']
q = [] #lowercase
s =[] #uppercase
spacial = [" ","!","'",'"',"#","$","%","&","(",")","*","+","-",",",".","/",";",":","<",">","=","@","{","}","|","^","~"]


for t in a:
	q.append(t)
for w in b:
	s.append(w)

# Started
# For Generate random password
try:
	j = int(input("if you want to generate random password please enter length of password otherwise press enter: "))
except:
	j = "2"
plain = ""
if int(j) >= 5 and int(j) <=20:
	for k in range(int(j)):
		sbc = ttt.randint(0,25)
		a = q[sbc]
		b = spacial[sbc]
		d = s[sbc]
		sbc = ttt.randint(0,9)
		c = g[sbc]
		
		plain = plain+a+b+c+d


	pass2 = plain[0:int(j)]
	print(pass2)
	
# check password strenth
else:

	def one(dkv):
		global er
		er = ["spe","int","low","upp","digit"]

		
		global pass2
		pass2 = input('Enter your password')#y.askpass(dkv,mask="-")
		global flag
		for v in pass2:
			if v in g:
				flag=flag+1
				er.remove("int")
				break

		for vv in pass2:
			if vv in q:
				flag=flag+1
				er.remove("low")
				break

		for v in pass2:
			if v in s:
				flag=flag+1
				er.remove("upp")
				break

		for v in pass2:
			if v in spacial:
				flag=flag+1
				er.remove("spe")
				break
		d = len(pass2)
		
		if d >= 8:
			er.remove("digit")
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


	dkv = "Enter your password: "
	one(dkv)
	while flag!=5:
		

		print("\n")
		print("just a moment we are checking")
		for j in er:



			if j == "int":
				bt.sleep(1)
				print("missing integer like 0,1,2,3...")

			if j == "spe":
				bt.sleep(1)
				print("missing special character like @,#,$,%...")
				

			if j == "low":
				bt.sleep(1)
				print("missing lowercase like 'a','b','c','d'...")
				

			if j == "upp":
				bt.sleep(1)
				print("missing uppercase like 'A','B','C','D'")
				

			if j == "digit":
				bt.sleep(1)
				print("your password must be 8 letters.")
				bt.sleep(1)


		trr = len(pass2)
		for b in range(8):
			sbc = ttt.randint(0,25)
			a = q[sbc]
			b = spacial[sbc]
			d = s[sbc]
			sbc = ttt.randint(0,9)
			c = g[sbc]
			
			pass2 = pass2+a+b+c+d

		br = "Checkup finished"
		print(br)
		print(end='')

		flag = 0
		print('\n')

		print("Suggested password: ",pass2[3:16])
		bt.sleep(3)
		dkv = "Enter your new password: "
		one(dkv)
# save password with name
def save():
	f = input("for save password enter name of account: ")
	ft = open(".password.txt","a")
	ft.write("\n")
	ft.write(f)
	ft.write(" : ")
	ft.write(pass2)
	ft.close()
	print("your password saved in password.txt.(file is hidden)")
save()

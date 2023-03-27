s = input()
c = "".join(set(s))
n = len(s)
v = 0
o = 1
r = ""
j = ""
for i in c:
	a = s.count(i)
	if a%2 == 0 :
		r +=i*(a//2)
	elif v == 0:
		j=i*a
		v=1
	else:
		o=0
		print("NO SOLUTION")
		break
if o==1:
	print(r+j+r[::-1])		

		



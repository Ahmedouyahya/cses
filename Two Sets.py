n=int(input())
s=n*(n+1)/2
if(s%2==0):
	print("YES")
	s1=s/2
	i=n
	l1=""
	l2=""
	nb=0
	np=0
	while (s1>=0 and i>0):
		if s1>=i :
			s1-=i
			l1=l1+" "+str(i)
			i-=1
			nb+=1
		else:
			l2=l2+" "+str(i)
			i-=1
			np+=1
	print(nb)
	print(l1[1:])
	print(np)
	print(l2[1:])
else:
	print("NO")
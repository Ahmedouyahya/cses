n=int(input())
nb=(n+1)//2
if(nb%2==0):
	print("YES")
	i=n
	j=n-1
	l1=[]
	l2=[]
	while(i > 0 and j > 0):
		l1.append(i)
		i=i-3
		if i>0 :
			l1.append(i)
			i=i-1
		l2.append(j)
		j=j-1
		l2.append(j)
		j=j-3
	print(n//2)
	for i in range(n//2):
		print(l1[i], end=" ")
	print()
	print((n+1)//2)
	for i in range((n+1)//2):
		print(l2[i], end=" ")
else:
	print("NO")
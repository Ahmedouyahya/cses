n = int(input())
for k in range(1, n+1):
    if k==1 :
    	print(0)
    if k==2 :
    	print(6)
    if k>=3 :
    	a = ((k**2)-5)*(k-3)*4
    	b = ((k**2)-7)*(k-4)*4
    	c = ((k**2)-4)*8
    	d = ((k**2)-9)*((k-4)**2)
    	e=((k**2)-3)*4
    	p=a+b+c+d+e
    	print(int(p/2))
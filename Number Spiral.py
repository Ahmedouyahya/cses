n = int(input())
L = []
for _ in range(n):
	L += list(map(int ,input().split()))
for i in range(0,n):
	x = L[2*i]
	y = L[2*i+1]
	m=max(x,y)
	if(m%2==0):
		s = 1+(m*(m-1))+(x-y)
	else:
		s = 1+(m*(m-1))-(x-y)
	print(s)

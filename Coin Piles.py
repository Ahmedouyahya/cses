n = int(input())
L = []
for _ in range(n):
	L += list(map(int ,input().split()))
for i in range(0,n):
	a = L[2*i]
	b = L[2*i+1]
	m = max(a,b)
	if((a+b)%3 == 0 and a >= m/2 and b >= m/2):
		print("YES")
	else:
		print("NO")
		
	
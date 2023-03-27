q = int(input())
s = ''.join(str(i) for i in range(1, 10 ** 6))
l=[]
for i in range(q):
    k = int(input())
    l.append(s[k-1])
for i in range(q):
	print(l[i])

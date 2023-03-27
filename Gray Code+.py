n = int(input())
s = 0
for i in range(n):
	s+=2**i
for i in range(0,s+1):
	print("0"*(n-len(bin(i)[2:])) + bin(i)[2:])
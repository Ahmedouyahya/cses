n = int(input())
L = ['0', '1']
for i in range(1, n):
    invL = L[::-1]
    L = ['0' + j for j in L]
    invL = ['1' + j for j in invL]
    L += invL

for i in L:
    print(i)
from itertools import permutations

s = input().strip()
n = len(s)
u = sorted(set(permutations(s, n)))
print(len(u))
for i in u:
    print(''.join(i))
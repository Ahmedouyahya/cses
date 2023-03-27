s = input().strip()
p = input().strip()
nb = 0
for i in range(len(s) - len(p) + 1):
    if s[i:i+len(p)] == p:
        nb += 1
print(nb)
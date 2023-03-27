dna = input()
max_len = 1
curr_len = 1

for i in range(1, len(dna)):
    if dna[i] == dna[i-1]:
        curr_len += 1
        max_len = max(max_len, curr_len)
    else:
        curr_len = 1

print(max_len)

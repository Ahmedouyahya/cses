q = int(input())
L = [int(input()) for _ in range(q)]
def position(k):
    n = 1
    while k > 9 * n * (10 ** (n-1)):
        k -= 9 * n * (10 ** (n-1))
        n += 1
    digit_num = (k-1) // n
    digit_pos = (k-1) % n
    digit = str(10**(n-1) + digit_num)[digit_pos]
    return int(digit)

for k in L:
    print(position(k))

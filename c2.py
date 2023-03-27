n = int(input())
nums = list(map(int, input().split()))
missing_num = (n * (n + 1))//2 - sum(nums)
print(missing_num)

n = int(input())
arr = list(map(int, input().split()))

res = min(arr)
now = 0

for i in arr:
    now = max(i, now + i)
    res = max(res, now)

print(res)
from bisect import bisect_left

n = int(input())
all = list()
for _ in range(n):
    a, b = map(int, input().split())
    all.append((a, 1))
    all.append((b, -1))

now = res = 0
all.sort()
for i in all:
    now += i[1]
    res = max(res, now)

print(res)

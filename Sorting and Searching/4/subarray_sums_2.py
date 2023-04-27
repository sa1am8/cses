n, x = map(int, input().split())
arr = list(map(int, input().split()))

used = {0: 1}
res = 0
s = 0

for i in arr:
    s += i

    if s - x in used:
        res += used[s - x]

    if s in used:
        used[s] += 1
    else:
        used[s] = 1



print(res)
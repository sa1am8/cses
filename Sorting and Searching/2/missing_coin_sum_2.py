n = int(input())
arr = sorted(list(map(int, input().split())))

res = 0
for i in arr:
    if res + 1 < i:
        break
    res += i

print(res + 1)
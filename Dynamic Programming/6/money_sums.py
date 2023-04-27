n = int(input())
coins = list(map(int, input().split()))

s = sum(coins)
res = [0] * (s+1)

res[0] = 1
for i in range(n):
    for value in reversed(range(coins[i], s+1)):
        res[value] |= res[value-coins[i]]

res = res[1:]
print(res.count(1))
for i in range(s):
    if res[i]:
        print(i+1, end=' ')

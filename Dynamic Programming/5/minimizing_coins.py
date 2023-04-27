n, x = map(int, input().split())
coins = list(map(int, input().split()))
value = [10**9] * (x+1)
value[0] = 0


for i in range(1, n+1):
    for w in range(x+1):
        if w - coins[i-1] >= 0:
            value[w] = min(value[w], value[w - coins[i-1]] + 1)

print(value[x] if value[x] != 10**9 else -1)

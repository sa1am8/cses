import sys
sys.setrecursionlimit(10**6)

INF = 10**9
a, b = map(int, input().split())
dp = [[INF]*501 for _ in range(501)]


def solve(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    if dp[a][b] != INF:
        return dp[a][b]
    if a == b:
        dp[a][b] = 0
        return 0
    if a == 1 or b == 1:
        dp[a][b] = b-1 if a == 1 else a-1
        return dp[a][b]
    for i in range(1, a):
        dp[a][b] = min(dp[a][b], solve(i, b) + solve(a-i, b) + 1)
    for i in range(1, b):
        dp[a][b] = min(dp[a][b], solve(a, i) + solve(a, b-i) + 1)
    return dp[a][b]

print(solve(a, b))
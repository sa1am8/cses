n = int(input())
c = [input() for i in range(n)]
dp = [[0 for j in range(n)] for i in range(n)]

dp[0][0] = (c[0][0] == '.')

for i in range(n):
    for j in range(n):
        if c[i][j] == '.':
            if i > 0 and c[i-1][j] == '.':
                dp[i][j] += dp[i-1][j]
            if j > 0 and c[i][j-1] == '.':
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= int(1e9+7)

print(dp[n-1][n-1])
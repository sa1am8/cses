import sys

input = sys.stdin.readline

n, q = map(int, input().split())
forest = [input() for i in range(n)]

prep = [[0] * (n+1) for i in range(n+1)]
prep[1][1] = 1 if forest[0][0] == '*' else 0

for i in range(2, n+1):
    prep[i][1] = prep[i - 1][1] + int(forest[i-1][0] == '*')
    prep[1][i] = prep[1][i - 1] + int(forest[0][i-1] == '*')

for i in range(2, n+1):
    for j in range(2, n+1):
        prep[j][i] = prep[j][i - 1] + prep[j - 1][i] - prep[j - 1][i - 1] + int(forest[j-1][i-1] == '*')

for i in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    print(prep[y2][x2] + prep[y1-1][x1-1] - prep[y1-1][x2] - prep[y2][x1-1])

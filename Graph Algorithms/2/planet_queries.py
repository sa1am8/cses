from sys import stdin

input = stdin.readline
MAXN = 2 * 10 ** 5 + 5
MAXD = 30
n, q = map(int, input().split())
parent = [[0 for _ in range(31)] for _ in range(MAXN)]


def jump(a, d):
    for i in range(MAXD):
        if d & (1 << i):
            a = parent[a][i]
    return a


data = list(map(int, input().split()))
for i in range(1, n + 1):
    parent[i][0] = data[i-1]


for d in range(1, MAXD):
    for i in range(1, n + 1):
        parent[i][d] = parent[parent[i][d - 1]][d - 1]

res = list()
while q:
    a, b = map(int, input().split())
    res.append(str(jump(a, b)))
    q -= 1

print(' '.join(res))

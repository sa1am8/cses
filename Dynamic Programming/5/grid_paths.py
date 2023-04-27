import sys
sys.setrecursionlimit(5000)


n = int(input())
been = [[0 for _ in range(n)] for i in range(n)]

path = list()
for i in range(n):
    path.append([i for i in input()])

def solve(x, y):
    if x == 0 and y == 0 and path[x][y] != '*':
        return 1

    if x == -1 or y == -1:
        return 0

    if path[x][y] == '*':
        return 0

    been[x][y] = 1
    s = 0
    s += solve(x-1, y) + solve(x, y - 1)
    return s

print(solve(n-1, n-1))

from sys import stdin, setrecursionlimit

"""
5 8
########
#..#...#
####.#.#
#..#...#
########
"""

input = stdin.readline
setrecursionlimit(20000)

add_x = [0, 0, -1, 1]
add_y = [-1, 1, 0, 0]

n, m = map(int, input().split())
data = [input() for i in range(n)]

visited = [[0 for _ in i] for i in data]


def is_valid(y, x):
    if x < 0 or y < 0:
        return False
    if y >= n or x >= m:
        return False
    return not data[y][x] == '#'


def dfs(i, j):
    if visited[i][j] == 1:
        return
    visited[i][j] = 1
    for k in range(4):
        y = i + add_x[k]
        x = j + add_y[k]
        if is_valid(y, x):
            if not visited[y][x]:
                dfs(y, x)


res = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == '.' and not visited[i][j]:
            dfs(i, j)
            res += 1

print(res)
from sys import stdin, setrecursionlimit

"""
4 2
1 2
3 4
"""

input = stdin.readline
setrecursionlimit(20000)

c, r = map(int, input().split())
edges = {}
seen = [0] * (c + 1)

for i in range(r):
    x, y = map(int, input().split())
    if x not in edges:
        edges[x] = []
    if y not in edges:
        edges[y] = []
    edges[x].append(y)
    edges[y].append(x)


def dfs(node):
    seen[node] = 1
    if node in edges:
        for i in edges[node]:
            if not seen[i]:
                dfs(i)


res = []
for j in range(1, c + 1):
    if not seen[j]:
        res.append(j)
        dfs(j)

print(len(res) - 1)
print('\n'.join([f"{res[i]} {res[i + 1]}" for i in range(len(res) - 1)]))

from sys import stdin, setrecursionlimit

# TLE by recusrion
setrecursionlimit(200000)
input = stdin.readline

"""
5 3
1 2
1 3
4 5
"""

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
group = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(node, prev):
    if group[node] != 0:
        return group[node] != prev

    group[node] = 1 if prev == 2 else 2
    for each in edges[node]:
        if not dfs(each, group[node]):
            return 0
    return 1


team = 1
flag = 1
for i in range(1, n + 1):
    if flag:
        flag = dfs(i, 0)

    else:
        break

if not flag:
    print("IMPOSSIBLE")
else:
    print(' '.join(map(str, group[1:])))

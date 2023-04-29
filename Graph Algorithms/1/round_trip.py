from sys import stdin, setrecursionlimit

setrecursionlimit(200000)
input = stdin.readline


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(node, path):
    if seen[node]:
        return path

    seen[node] = 1
    for each in edges[node]:
        if each == node:
            continue
        dfs(each, path+[node])



for i in range(1, n+1):
    seen = [0] * (n + 1)
    a = dfs(i, [])
    print(a)


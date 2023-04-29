# Flight Routes (TLE)
from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
dist = [[float('inf')] * k for _ in range(n + 1)]
dist[1][0] = 0

for _ in range(m):
    u, v, c = map(int, input().split())
    g[u].append((v, c))


def dij():
    pq = [(0, 1)]
    visited = [False] * (n + 1)
    while pq:
        d, u = min(pq)
        pq.remove((d, u))

        if dist[u][k - 1] < d:
            continue

        visited[u] = True

        for v, c in g[u]:
            if dist[v][k - 1] > c + d:
                dist[v][k - 1] = c + d
                pq.append((dist[v][k - 1], v))
                dist[v].sort()


dij()

print(' '.join([dist[n][i] for i in range(k)]))

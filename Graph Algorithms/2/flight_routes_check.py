from sys import stdin

input = stdin.readline

"""
4 5
1 2
2 3
3 1
1 4
3 4
"""

n, m = map(int, input().split())
edges = {}
for _ in range(m):
    a, b = map(int, input().split())
    if a not in edges:
        edges[a] = []

    edges[a].append(b)


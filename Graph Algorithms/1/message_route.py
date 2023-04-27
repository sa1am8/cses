from sys import stdin
from collections import deque

"""
5 5
1 2
1 3
1 4
2 3
5 4
"""

input = stdin.readline

n, m = map(int, input().split())
edges = {}

for _ in range(m):
    x, y = map(int, input().split())
    if x not in edges:
        edges[x] = []
    if y not in edges:
        edges[y] = []
    edges[x].append(y)
    edges[y].append(x)

seen = [0 for i in range(n + 1)]
parent = [None for _ in range(n + 1)]

deq = deque()
deq.append(1)

if 1 not in edges:
    print("IMPOSSIBLE")
    exit()

while deq:
    node = deq.popleft()

    if seen[node]:
        continue

    seen[node] = 1
    for i in edges[node]:
        if seen[i]:
            continue

        if i == n:
            parent[i] = node
            res = []
            while i:
                res.append(str(i))
                i = parent[i]
            print(len(res), ' '.join(res[::-1]), sep='\n')
            exit()

        if parent[i] is None:
            parent[i] = node
            deq.append(i)


print("IMPOSSIBLE")

from collections import deque
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())

edges = [[] for _ in range(n+1)]
queue = deque()
in_degree = [0] * (n+1)
order = []


for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    curr = queue.popleft()
    order.append(curr)
    for neighbor in edges[curr]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

if len(order) != n:
    print("IMPOSSIBLE")
else:
    print(*order)
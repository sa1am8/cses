from sys import stdin
from collections import deque

input = stdin.readline
inf = 10**8

class PriorityQueue(object):
    def __init__(self):
        self.queue = deque()

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def push(self, data):
        for i in range(len(self.queue)):
            if self.queue[i][0] > data[0]:
                self.queue.insert(i, data)
                return
        self.queue.append(data)

    def pop(self):
        try:
            item = self.queue.popleft()
            return item
        except IndexError:
            raise IndexError("pop from an empty priority queue")

    def top(self):
        try:
            return self.queue[0]
        except IndexError:
            raise IndexError("top from an empty priority queue")


"""
4 6 3
1 2 1
1 3 3
2 3 2
2 4 6
3 2 8
3 4 1
"""
n, m, k = map(int, input().split())

q = PriorityQueue()

edges = {}
processed = [0] * (n + 1)
distance = [inf] * (n + 1)

for _ in range(m):
    x, y, c = map(int, input().split())
    if x not in edges:
        edges[x] = list()
    edges[x].append((y, c))

q.push((1, 0))
distance[1] = 0

while not q.isEmpty():
    a = q.pop()[0]

    if a == n:
        break

    if processed[a]:
        continue
    processed[a] = 1

    for i in edges[a]:
        b, w = i
        if distance[a] + w < distance[b]:
            distance[b] = distance[a] + w
            q.push((distance[b], b))

print(distance)
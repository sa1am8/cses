n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))


def find_k_shortest_paths(graph, start, end, k):
    paths = [(0, [start])]

    while len(paths) < k:
        if not paths:
            return []

        cost, path = min(paths)
        paths.remove((cost, path))

        if path[-1] == end:
            yield cost, path

        for node, weight in graph[path[-1]]:
            paths.append((cost + weight, path + [node]))


for cost, path in find_k_shortest_paths(graph, 0, n - 1, k):
    print(cost, end=" ")

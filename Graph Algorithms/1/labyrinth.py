from sys import stdin
from collections import deque

"""
5 8
########
#.A#...#
#.##.#B#
#......#
########
"""

input = stdin.readline
diff_row = [-1, 0, 1, 0]
diff_col = [0, 1, 0, -1]

n, m = map(int, input().split())
data = [input() for i in range(n)]

start, end = 0, 0
for i in range(n):
    if start and end:
        break
    for j in range(m):
        if data[i][j] == "A":
            start = i, j
        elif data[i][j] == "B":
            end = i, j

deq = deque()
deq.append(start)
seen = [[False for _ in range(m)] for _ in range(n)]
seen[start[0]][start[1]] = True
parent = [[None for _ in range(m)] for _ in range(n)]

while deq:
    i, j = deq.popleft()

    if (i, j) == end:
        path = []
        while parent[i][j] is not None:
            direction = parent[i][j]
            path.append('URDL'[direction])
            i += diff_row[(direction + 2) & 3]
            j += diff_col[(direction + 2) & 3]

        print("YES", len(path), ''.join(path[::-1]), sep='\n')
        exit()

    for direction in range(4):
        r = i + diff_row[direction]
        c = j + diff_col[direction]
        if 0 <= r < n and 0 <= c < m and data[r][c] != '#' and not seen[r][c]:
            parent[r][c] = direction
            deq.append((r, c))
            seen[r][c] = True

print('NO')

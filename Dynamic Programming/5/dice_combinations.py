import sys

sys.setrecursionlimit(10 ** 7)

n = int(input())
values = [i for i in range(1, 6 + 1)]
m = 10 ** 9 + 7
used = {0: 1}


def solve(x):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    if x in used:
        return used[x]

    s = 0
    for i in values:
        s += solve(x - i)
        s %= m

    used[x] = s
    return s


print(solve(n))

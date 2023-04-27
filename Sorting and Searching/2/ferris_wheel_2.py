from bisect import bisect_right
import sys

n, x = map(int, sys.stdin.readline().split())
wt = sorted(map(int, sys.stdin.readline().split()))

res = 0
i = 0
used = set()

while len(wt) > 1:
    if i == len(wt):
        break

    bis = bisect_right(wt, x - wt[i]) - 1
    bis += 1 if i == bis and i < len(wt) else 0

    #if bis == len(wt):
    #    break

    print(wt, bis, i)

    if wt[i] + wt[bis] <= x:

        used.add(bis)
        i += 1
        res += 1
    else:
        break

sys.stdout.write(str(res))

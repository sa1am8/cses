from bisect import bisect_right
from itertools import combinations



n = int(input())
arr = sorted(list(map(int, input().split())))

comb = set()

for i in range(1, sum(arr) + 2):
    if i in arr:
        continue

    elif i not in comb:
        bis = bisect_right(arr, i)

        if bis >= n:

            bis = n - 1
            print(sum(arr) + 1)
            break

        for j in range(bis+1):
            for k in set(map(sum, combinations(arr[:bis], j))):
                comb.add(k)

        comb = set(comb)

        if i not in comb:
            print(i)
            break

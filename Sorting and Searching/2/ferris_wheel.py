import sys


def binary_search(arr, low, high, x, used):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == x:

            if mid == len(arr) - 1 and mid not in used:
                return mid

            while arr[mid + 1] == arr[mid] and mid not in used:
                if mid + 1 == len(arr) - 1 and mid + 1 not in used:
                    return mid + 1
                mid += 1

            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x, used)

        return binary_search(arr, mid + 1, high, x, used)

    if (low + high) // 2 in used:

        return 0

    return (low + high) // 2


n, x = map(int, sys.stdin.readline().split())
wt = sorted(map(int, sys.stdin.readline().split()))

used = set()
res = i = 0

p = binary_search(wt, 0, len(wt) - 1, x - wt[0], used) - n

while len(wt) > 1:

    if abs(p) >= len(wt) or p == 0 or i + abs(p) >= len(wt):
        break

    if wt[i] + wt[p] <= x:
        #print(wt, i, p)
        i += 1
        used.add(n + p)

        res += 1
        p -= 1

        if p * (-1) == len(wt) + 1:
            break
        continue

    p = binary_search(wt, 0, len(wt) - 1, x - wt[i], used) - n


sys.stdout.write(str((len(wt) - res)))

import sys


def binary_search(arr, low, high, x, k):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] - k <= x <= arr[mid] + k:
            while arr[mid - 1] - k <= x <= arr[mid - 1] + k and mid != 0:
                mid -= 1

            return mid

        elif arr[mid] + k > x:
            return binary_search(arr, low, mid - 1, x, k)

        return binary_search(arr, mid + 1, high, x, k)

    return -1

for i, line in enumerate(sys.stdin):
    if i == 0:
        n, m, k = map(int, line.rstrip().split())
    if i == 1:
        des = sorted(list(map(int, line.rstrip().split())))
    if i == 2:
        apartments = map(int, line.rstrip().split())
        break


res = 0
index = -1

for ap in apartments:

    index = binary_search(des, 0, len(des) - 1, ap, k)

    if index != -1:

        res += 1
        del des[index]

sys.stdout.write(str(res))


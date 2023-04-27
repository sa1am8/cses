n, x = map(int, input().split())
arr = list(map(int, input().split()))

f, s = 0, 1
res = arr[0]
c = 0

while f < n or s < n:
    if s == n:
        if res == x:
            c += 1
            break

        if res < x:
            break

        else:
            f += 1
            res -= arr[f - 1]
            continue

    if res > x:
        f += 1
        res -= arr[f-1]
    elif res < x:
        s += 1
        res += arr[s-1]
    else:
        c += 1
        s += 1
        res += arr[s - 1]

print(c)
t = int(input())

for _ in range(t):
    y, x = map(int, input().split(' '))

    dy = (int(y) ** 2) * ((y + 1) % 2) + (int(y-1) ** 2) * (y % 2) + y % 2
    dx = (int(x) ** 2) * (x % 2) + (int(x-1) ** 2) * ((x + 1) % 2) + (1 + x) % 2

    if y > x:
        res = dy + ((-1) ** ((y + 1) % 2)) * x + (-1) ** (y % 2)

    elif x > y:
        res = dx + ((-1) ** (x % 2)) * y + (-1) ** ((x+1) % 2)

    else:
        res = (dx + dy) // 2

    print(res)
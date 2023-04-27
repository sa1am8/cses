for _ in range(int(input())):
    a, b = map(int, input().split())
    if (2*a - b) < 0 or (2*b - a) < 0:
        print("NO")
        continue
    print("YES" if (2*a - b) % 3 == 0 and (2*b - a) % 3 == 0 else "NO")
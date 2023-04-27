from math import log

n = int(input())
pw = log(n + 1, 2) - 1
p = n / 4
c = (n - 3) / 4

if pw % 1 == 0 and n != 1:
    print("YES")
    f = ["1", "2"]
    s = ["3"]
    addit = 1 if pw >= 3 else 0

    for i in range(1, int(pw) + addit):
        f.append(str(i * 4))
        f.append(str(i * 4 + 3))
        s.append(str(i * 4 + 1))
        s.append(str(i * 4 + 2))

    print(len(f))
    print(' '.join(f))
    print(len(s))
    print(' '.join(s))
    exit()

if p % 1 == 0 and n not in [1, 3]:
    f, s = list(), list()
    print("YES")

    for i in range(int(p)):
        f.append(str(i * 4 + 1))
        f.append(str(i * 4 + 4))
        s.append(str(i * 4 + 2))
        s.append(str(i * 4 + 3))

    print(len(f))
    print(' '.join(f))
    print(len(s))
    print(' '.join(s))
    exit()

if c % 1 == 0:
    print("YES")
    f = ["1", "2"]
    s = ["3"]

    for i in range(1, int(c) + 1):
        f.append(str(i * 4))
        f.append(str(i * 4 + 3))
        s.append(str(i * 4 + 1))
        s.append(str(i * 4 + 2))

    print(len(f))
    print(' '.join(f))
    print(len(s))
    print(' '.join(s))
    exit()


print("NO")
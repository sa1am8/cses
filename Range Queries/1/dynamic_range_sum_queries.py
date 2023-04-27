import sys

input = sys.stdin.readline
inf = 0

def sumq(a, b):
    a += length
    b += length
    res = 0
    while a <= b:
        if a % 2 == 1:
            res += tree[a]
            a += 1
        if b % 2 == 0:
            res += tree[b]
            b -= 1

        a //= 2
        b //= 2

    return res

def update(k, x):
    k += length
    tree[k] = x
    k //= 2
    while k >= 1:
        tree[k] = tree[2*k] + tree[2*k+1]
        k //= 2


n, q = map(int, input().split())
data = list(map(int, input().split()))


length = 2**(n-1).bit_length()
tree = [inf] * length + data + [inf] * (length - n)

for i in reversed(range(1, length)):
    tree[i] = tree[2*i] + tree[2*i+1]

res = list()

for i in range(q):
    x, y = map(int, input().split())
    if command-1:
        res.append(sumq(x-1, y-1))
    else:
        update(x-1, y)

print(*res, sep='\n')
n = int(input())
res = [n]
while res[-1] != 1:
    res.append(int(res[-1]) / 2 if res[-1] % 2 == 0 else res[-1] * 3 + 1)
print(' '.join(str(i) if '.' not in str(i) else str(i).split('.')[0] for i in res))
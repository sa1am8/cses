n = int(input())
print('\n'.join(f'{(i^(i>>1)):016b}'[-n:] for i in range(2**n)))
exit()

# trying
r = [['0'] * n]
rs = [['0'] * (2 ** (n - 1)) + ['1'] * 2 ** (n - 1)]
res = [[] for i in range(n)]
res[0] = rs[0]

for i in range(1, n):
    r = ['0'] * (2 ** (n - i - 1)) + ['1'] * 2 ** (n - i - 1)
    b = ['1'] * (2 ** (n - i - 1)) + ['0'] * 2 ** (n - i - 1)
    rs.append([r + b if not j % 2 else b + r for j in range(i)])
    print([r + b if not j % 2 else b + r for j in range(i)])

    for j in rs[i]:
        res[i] += j

[print(len(res[i])) for i in range(n)]

for i in range(2 ** n):
    d = ''.join([res[j][i % len(res[j])] for j in range(n)])
    print(d)




# -1 - every 1 times
# -2 - every 2 times
# -3 - every 3 times



n = int(input())
if 2 <= n <= 3:
    print('NO SOLUTION')
    exit()

print(' '.join([str(i) for i in range(2, n+1, 2)] + [str(i) for i in range(1, n+1, 2)]))
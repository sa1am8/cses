def f(i):
    return 9 * i * 10 ** (i - 1)


for _ in range(int(input())):

    n = int(input())

    j = 0

    while True:
        j += 1
        if f(j - 1) <= n <= f(j):
            break



    num = n - f(j - 1) - 1  # num of i-digits numbers
    val = 10 * (j - 1) + (num // j)  # exactly numb

    print(n, j)
    print(str(val))

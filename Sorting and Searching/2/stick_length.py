n = int(input())
arr = list(map(int, input().split()))

if n % 2 == 1:
    mid = sorted(arr)[n // 2]
    print(sum([abs(i - mid) for i in arr]))
    exit()
else:
    mid1 = sorted(arr)[n // 2]
    mid2 = sorted(arr)[n // 2 + 1]
    print(int(min(sum([abs(i - mid1) for i in arr]),
                  sum([abs(i - mid2) for i in arr]))))

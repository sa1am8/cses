n = int(input())
arr = list(map(int, input().split()))


res = 1
for i in range(1, n):
    if arr[i-1] > arr[i]:
        res += 1

print(res)
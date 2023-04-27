from bisect import bisect_right

n = int(input())
arr = list(map(int, input().split()))

res = [arr[0]]

for i in arr[1:]:
    index = bisect_right(res, i)
    if index == len(res):
        res.append(i)
    else:
        res[index] = i

print(len(res))
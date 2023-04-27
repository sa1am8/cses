


from bisect import bisect_right
#from sortedcontainers import SortedList

n, x = map(int, input().split())
arr = list(map(int, input().split()))

adding = [0, n]
ans = [n]

for i in arr:
    index = bisect_right(adding, i)
    l = adding[index-1]
    r = adding[index]
    del ans[ans.index(r-l)]

    adding.insert(index, i)
    ans.append(i-l)
    ans.append(r-i)
    print(max(ans))


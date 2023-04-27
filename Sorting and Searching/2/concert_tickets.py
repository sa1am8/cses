from bisect import bisect_right

n, m = map(int, input().split())
tickets = sorted(map(int, input().split()))
customers = list(map(int, input().split()))

#with open('test') as f:
#    n, m = map(int, f.readline().split())
#    tickets = sorted(map(int, f.readline().split()))
#    customers = list(map(int, f.readline().split()))

used = set()

for c in customers:

    if len(used) == len(tickets):
        print(-1)
        continue

    i = bisect_right(tickets, c) - 1

    if i == -1:
        print(-1)
        continue

    while i in used and i >= 0:
        i -= 1

    if i == -1:
        print(-1)
        continue

    #print(tickets, c, tickets[i], i, used)
    used.add(i)
    print(tickets[i])
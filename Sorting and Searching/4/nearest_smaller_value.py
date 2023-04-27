n = int(input())
arr = list(map(int, input().split()))

gr = list()
for i in range(n):
    while len(gr) != 0 and arr[gr[-1]] >= arr[i]:
        gr.pop()

    if not gr:
        print('0', end=' ')

    else:
        print(gr[-1] + 1, end=' ')

    gr.append(i)

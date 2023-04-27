n, x = map(int, input().split())
lst = list(map(int, input().split()))

srt = sorted(lst)

l = 0
r = len(srt) - 1

while l < len(srt) and r > 0:
    if srt[l] + srt[r] == x and r != l:
        f = lst.index(srt[l]) + 1
        if srt[l] == srt[r]:
            s = lst[f:].index(srt[r]) + 1 + f
        else:
            s = lst.index(srt[r]) + 1

        print(f, s)
        exit()

    elif srt[l] + srt[r] > x:
        r -= 1

    else:
        l += 1

print("IMPOSSIBLE")
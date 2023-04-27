n, m, k = map(int, input().split())
des = list(sorted(map(int, input().split())))
ap = list(sorted(map(int, input().split())))
c_p = a_p = res = 0

while c_p < len(des) and a_p < len(ap):
    if abs(ap[a_p] - des[c_p]) <= k:
        a_p += 1
        c_p += 1
        res += 1
        continue
    if ap[a_p] < des[c_p] + k:
        a_p += 1
    else:
        c_p += 1

print(res)
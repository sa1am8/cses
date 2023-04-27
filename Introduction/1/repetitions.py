string = input() + '1'
res = 1
i, j = 0, 1
_len = len(string)

while j < len(string):
    if string[j] == string[i]:
        j += 1
    else:
        res = max(res, j - i)
        i = j
        j += 1

print(res)
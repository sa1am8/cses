string = input()
u, res = '', ''

for i in set(string):
    c = string.count(i)
    if not c % 2:
        res += i * (c // 2)
    elif not u:
        u = i * c
    else:
        print("NO SOLUTION")
        exit()

print(res + u + res[::-1])
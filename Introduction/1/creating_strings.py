def fact(i):
    res = 1
    for i in range(1, i+1):
        res *= i
    return res

string = input()
count = fact(len(string))
for i in set(string):
    count //= fact(string.count(i))

print(count)
ln = len(string)

letters = list(string)
letters.sort()
print(letters)
res = list()

def get_all_prefix(lst, prefix=""):

    if len(prefix) == len(lst):
        print(prefix)
        res.append(prefix)
        return res

    for i in range(len(lst)):
        prefix = prefix + lst[i]
        get_all_prefix([j for j in lst if j != i], prefix)

get_all_prefix(letters)

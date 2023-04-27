n = int(input())
numbers = list(map(int, input().split(' ')))
res = 0

for i in range(1, n):
    if numbers[i-1] > numbers[i]:
        add = (numbers[i-1] - numbers[i])
        numbers[i] += add
        res += add

print(res)
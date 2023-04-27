n = int(input())
string = list(map(int, input().split(' ')))
string.sort()

if string[0] != 1:
    print(1)
    exit()

if string[-1] != n:
    print(n)
    exit()


for j in range(1, n-1):
    if string[j] - string[j-1] != 1:
        print(string[j] - 1)


#print(j for j in range(1, n+1) if f' {str(j)} ' not in string)
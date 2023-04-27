n = int(input())

circle = list(range(1, n+1))
k = 1
index = k


while len(circle) > 1:
    print(circle[index], end=" ")
    circle.pop(index)
    index = (index + k) % len(circle)

print(circle[0])

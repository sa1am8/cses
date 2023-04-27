n, q = map(int, input().split())
x = list(map(int, input().split()))

prefix_sum = [0] * (n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] ^ x[i-1]

for i in range(q):
    a, b = map(int, input().split())
    print(abs(prefix_sum[b] ^ prefix_sum[a-1]))
x = int(input())

d = [0] * (x + 1)
a = [0] * (x + 1)

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    a[i] = i - 1

    if i % 2 == 0 and d[i] > (d[i // 2] + 1):
        d[i] = d[i // 2] + 1
        a[i] = i // 2
    if i % 3 == 0 and d[i] > (d[i // 3] + 1):
        d[i] = d[i // 3] + 1
        a[i] = i // 3

print(d[x])

while x != 1:
    print(x, end=" ")
    x = a[x]
print(x)

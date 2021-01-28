A = int(input())
B = int(input())
C = int(input())
sum = A * B * C
res = list(str(sum))
for i in range(10):
    print(res.count(str(i)))

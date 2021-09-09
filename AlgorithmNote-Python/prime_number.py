import math


# 소수 판별 알고리즘
def is_prime_number(n):
    # for i in range(2, n): 이렇게 하면 시간이 오래 걸림
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 에라토스테네스의 체

n = 1000
arr = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(2, n+1):
    if arr[i]:
        print(i, end=' ')

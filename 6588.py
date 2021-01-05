import sys


# 1000000까지의 홀수 소수 구하기
def findprime(n):
    numlist = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if numlist[i]:
            for j in range(i+i, n, i):
                numlist[j] = False

    return numlist


# 골드바흐 판별
def goldbach(n):
    for i in range(3, n):
        if primes[i]:
            if primes[n-i]:
                print("{} = {} + {}".format(n, i, n - i))
                break


primes = findprime(1000000)

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break

    goldbach(num)
import sys

N, K = map(int, sys.stdin.readline().split())
count = 0

while N != 1:
    if N % K == 0:
        count += 1
        N = N // K
    else:
        count += (N % K)
        N -= (N % K)

print(count)

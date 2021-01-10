import sys
import time

N, K = map(int, sys.stdin.readline().split())
count = 0

start_time = time.time()
while N != 1:
    if N % K == 0:
        count += 1
        N = N // K
    else:
        count += (N % K)
        N -= (N % K)
end_time = time.time()

print(end_time - start_time)
print(count)

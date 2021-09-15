import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

for row in num_list:
    result = max(result, min(row))

print(result)

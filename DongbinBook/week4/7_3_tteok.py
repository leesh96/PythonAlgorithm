import sys
N, M = map(int, input().split())
tteoks = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(tteoks)
res = 0

while start <= end:
    mid = (start + end) // 2
    cut_length = 0
    for tteok in tteoks:
        if tteok > mid:
            cut_length += tteok - mid
    if cut_length < M:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
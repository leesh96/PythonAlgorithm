import sys

sys.setrecursionlimit(10000)

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
plus, minus, mul, div = map(int, input().split())

max_result = -10e9
min_result = 10e9
plus_cnt, minus_cnt, mul_cnt, div_cnt = 0, 0, 0, 0
cur_idx = 0


def dfs(num, idx):
    global plus_cnt, minus_cnt, mul_cnt, div_cnt, cur_idx
    global max_result, min_result

    if idx == n-1:
        max_result = max(num, max_result)
        min_result = min(num, min_result)
        plus_cnt, minus_cnt, mul_cnt, div_cnt = 0, 0, 0, 0
        idx = 0
        return

    next = idx + 1

    if plus_cnt < plus:
        plus_cnt += 1
        dfs(num + array[next], next)
    if minus_cnt < minus:
        minus_cnt += 1
        dfs(num - array[next], next)
    if mul_cnt < mul:
        mul_cnt += 1
        dfs(num * array[next], next)
    if div_cnt < div:
        div_cnt += 1
        dfs(num / array[next], next)


dfs(array[0], 0)
print(max_result, min_result, sep='\n')

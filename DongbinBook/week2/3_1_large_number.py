import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
numbers.sort(reverse=True)
first_num = numbers[0]
second_num = numbers[1]

count = M // (K + 1)
div = M % (K + 1)
result = (first_num * K + second_num) * count + first_num * div

print(result)

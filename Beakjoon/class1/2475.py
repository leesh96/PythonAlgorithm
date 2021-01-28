import sys

num_list = list(map(int, sys.stdin.readline().split()))
square_sum = 0

for num in num_list:
    square_sum += num**2

print(square_sum % 10)

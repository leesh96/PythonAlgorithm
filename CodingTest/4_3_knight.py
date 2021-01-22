import sys

x_direction = [2, 2, -2, -2, 1, 1, -1, -1]
y_direction = [1, -1, 1, -1, 2, -2, 2, -2]

input = list(sys.stdin.readline())
a = input[0]
b = int(input[1])
count = 0

for i in range(8):
    a_next = ord(a) + x_direction[i]
    b_next = b + y_direction[i]
    if (ord('a') <= a_next <= ord('h')) and (1 <= b_next <= 8):
        count += 1

print(count)

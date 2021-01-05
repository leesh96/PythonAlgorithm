import sys
from collections import deque

x_direction = [1, -1, 0, 0]
y_direction = [0, 0, 1, -1]


def bfs():
    global Q
    day = -1

    while Q:
        day += 1
        for _ in range(len(Q)):
            x, y = Q.popleft()
            for i in range(4):
                x_next = x + x_direction[i]
                y_next = y + y_direction[i]
                if (0 <= x_next < N) and (0 <= y_next < M):
                    if box[x_next][y_next] == 0:
                        box[x_next][y_next] = 1
                        Q.append((x_next, y_next))
    for row in box:
        if 0 in row:
            return -1
    return day


M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append((i, j))

print(bfs())

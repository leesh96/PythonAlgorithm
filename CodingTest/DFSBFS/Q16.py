import sys
import copy
from collections import deque

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
lab = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

size = n*m
virus_cnt = 0
Q = deque()

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus_cnt += 1
            Q.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 10e9


def make_wall(arr, start_x, start_y, wall_cnt):
    global result
    if wall_cnt == 0:
        print(temp)
        result = min(result, bfs(arr))
        return
    else:
        for x in range(start_x, n):
            for y in range(start_y, m):
                if arr[x][y] == 0:
                    arr[x][y] = 1
                    wall_cnt -= 1
                    make_wall(arr, x, y, wall_cnt)


def bfs(arr):
    global virus_cnt
    global Q

    while Q:
        x, y = Q.popleft()
        visit[x][y] = True
        for i in range(4):
            x_next = x + dx[i]
            y_next = y + dy[i]
            if 0 <= x_next < n and 0 <= y_next < m:
                if arr[x_next][y_next] == 0 and not visit[x_next][y_next]:
                    arr[x_next][y_next] = 2
                    visit[x_next][y_next] = True
                    virus_cnt += 1
                    Q.append((x_next, y_next))

    return virus_cnt


for i in range(n):
    for j in range(m):
        temp = copy.deepcopy(lab)
        make_wall(temp, i, j, 3)

print(size - result - 3)

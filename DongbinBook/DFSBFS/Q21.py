import sys
from collections import deque

n, l, r = map(int, input().split())
a = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0


def bfs(x, y):
    global cnt
    global union
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            x_next = x + dx[i]
            y_next = y + dy[i]
            if 0 <= x_next < n and 0 <= y_next < n:
                if l <= abs(a[x][y] - a[x_next][y_next]) <= r and not visit[x_next][y_next]:
                    Q.append((x_next, y_next))
                    union.add((x, y))
                    union.add((x_next, y_next))
        visit[x][y] = True

    if union:
        return True
    else:
        return False


while True:
    temp_res = bfs(0, 0)
    if not temp_res:
        print(cnt)
        break
    else:
        population = sum(a[x][y] for x, y in union)
        for x, y in union:
            a[x][y] = population // len(union)
        cnt += 1
        union.clear()
        print(a)

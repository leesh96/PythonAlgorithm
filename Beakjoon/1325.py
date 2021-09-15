import sys
from collections import deque

"""
플랫폼 : 백준
문제번호 : 1325
문제제목 : 효율적인 해킹
난이도 : 실버 2
제한사항 : 5초/256MB
알고리즘 분류 : 그래프 이론, 그래프 탐색

알고리즘 설명
 1. 해킹할 수 있는 컴퓨터간의 신뢰하는 관계를 인접 그래프로 나타냄
 2. dfs(또는 bfs)를 돌면서 노드 방문 횟수를 count -> answer 배열의 값 증가
 3. dfs를 돌면서 방문하는 노드가 곧 함께 해킹할 수 있는 컴퓨터이기 때문
 4. answer 배열에서 max값을 찾고 max값과 같은 컴퓨터 번호 출력
 자바로 하면 dfs와 bfs 모두 시간초과. 동일 코드로 pypy3에서 시간초과 안남

채점 결과 : 11820ms/226320KB pypy3
풀이 날짜 : 2021/09/15
"""

n, m = map(int, sys.stdin.readline().rstrip().split())
answer = []
computer = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    computer[b].append(a)


def bfs(start):
    visit = [False] * (n + 1)
    visit[start] = True
    count = 0
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        for adj in computer[cur]:
            if not visit[adj]:
                visit[adj] = True
                count += 1
                q.append(adj)

    return count


for i in range(1, n+1):
    answer.append(bfs(i))

max_hack = max(answer)

for i in range(0, n):
    if answer[i] == max_hack:
        print(i + 1, end=' ')

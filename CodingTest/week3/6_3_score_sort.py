N = int(input())
scores = []
for _ in range(N):
    name, score = input().split()
    scores.append((name, int(score)))

scores.sort(key=lambda x: x[1])

for score in scores:
    print(score[0], end=' ')

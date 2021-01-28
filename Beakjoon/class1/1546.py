N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
for i in range(len(scores)):
    scores[i] /= max_score
    scores[i] *= 100
print(sum(scores) / N)

rests = []
for _ in range(10):
    n = int(input()) % 42
    if n in rests:
        continue
    else:
        rests.append(n)
print(len(rests))
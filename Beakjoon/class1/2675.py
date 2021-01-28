T = int(input())
for _ in range(T):
    R, S = input().split()
    n = int(R)
    P = ""
    for ch in S:
        P += ch * n
    print(P)
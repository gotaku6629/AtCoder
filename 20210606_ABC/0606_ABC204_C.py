N, M = map(int, input().split())

AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

for s in range(N):
    for g in range(N):
        for i in range(M):
            ...
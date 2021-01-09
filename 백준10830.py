import sys

N, B = map(int, sys.stdin.readline().split())
A = list(list(map(int, sys.stdin.readline().split()))for _ in range(N))
ans = list(list(1 for _ in range(N))for __ in range(N))

def mulProc(l1, l2):
    p = list(list(0 for _ in range(N))for __ in range(N))

    for i in range(N):
        for j in range(N):
            for k in range(N):
                p[i][j] += l1[i][k]*l2[k][j]
            p[i][j] %= 1000
    
    return p

def solution(a, b):
    if b == 1:
        return a

    else:
        p = solution(a, b//2)

        if b%2 == 0:
            return mulProc(p, p)
        else:
            return mulProc(mulProc(p, p), a)

for i in range(N):
    for j in range(N):
        A[i][j] %= 1000

ans = solution(A, B)
for i in ans:
    print(*i)
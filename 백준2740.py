import sys

N ,M = map(int, sys.stdin.readline().split())
A = list(list(map(int, sys.stdin.readline().split()))for _ in range(N))
M ,K = map(int, sys.stdin.readline().split())
B = list(list(map(int, sys.stdin.readline().split()))for _ in range(M))

for n in range(N):
    for k in range(K):
        anser = 0
        for m in range(M):
            anser += (A[n][m] * B[m][k])
    
        print(anser, end = ' ')
    print()
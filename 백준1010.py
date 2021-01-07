import sys

def NoC(n, m):
    n1 = 1
    n2 = 1
    
    for i in range(m, m-n, -1):
        n1 *= i

    for i in range(1, n+1):
        n2 *= i
    
    return n1//n2

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(NoC(N, M))

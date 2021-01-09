import sys

n = int(sys.stdin.readline())
proc = [[1, 1], [1, 0]]

def mulProc(l1, l2):
    p = list(list(0 for _ in range(2))for __ in range(2))

    for i in range(2):
        for j in range(2):
            for k in range(2):
                p[i][j] += l1[i][k]*l2[k][j]
            p[i][j] %= 1000000007
    
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


print(solution(proc, n)[0][1])

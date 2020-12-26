import sys

def solution(a, b, c):
    if b == 1:
        return a % c
    
    else:
        p = solution(a, b//2, c)
        if b%2==0:
            return p * p % c
        else:
            return p * p * a % c
            

A, B, C = map(int, sys.stdin.readline().split())

print(solution(A, B, C))
import sys

def GCD(a,b):
    if b==0: return a
    else: return GCD(b, a%b) 

def LCM(a, b):
    return a*b//GCD(a,b)


n = int(sys.stdin.readline())

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print(LCM(A, B))

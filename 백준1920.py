import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))

def divSort(a, find, l, r):
    ans = 0

    while l <= r:
        mid = (l+r)//2
        
        if a[mid] > find:
            r = mid-1
        
        elif a[mid] < find:
            l = mid +1
        
        else:
            ans = 1
            break

    return ans

A.sort()

for i in Ms:
    print(divSort(A, i, 0, (N-1)))
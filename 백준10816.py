import sys
N = int(sys.stdin.readline())
Ns = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))

def lowerBinary(arr, target, start, end):

    while end > start:
        mid = (start+end)//2
        if arr[mid] >= target:
            end = mid
        
        else:
            start = mid+1
    return end

def upperBinary(arr, target, start, end):
    while end > start:
        mid = (start+end)//2
        if arr[mid] > target:
            end = mid
        
        else:
            start = mid+1

    return end

Ns.sort()
Ns.append(10000001)
for i in Ms:
    lB = lowerBinary(Ns, i, 0, N)
    uB = upperBinary(Ns, i, 0, N)
    cnt = uB-lB
    print(cnt, end = ' ')
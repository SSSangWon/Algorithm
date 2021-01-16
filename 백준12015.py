import sys
r = sys.stdin.readline

N = int(r())
A = list(map(int, r().split()))

aList = [A[0]]
aCnt = 1

for i in range(1, N):
    start, end, target = 0, aCnt, A[i]

    while start < end:
        mid = (start+end)//2
        if target > aList[mid]:
            start = mid+1
        else:
            end = mid
    
    if aCnt <= end:
        aList.append(target)
        aCnt += 1
    else:
        aList[end] = target

    
print(aCnt)
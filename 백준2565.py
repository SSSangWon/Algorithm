def BS(lis, k):
    lo = 0
    hi = len(lis)-1

    while (hi-lo) > 0:
        mid = (lo+hi) // 2
        
        if lis[mid] < k:
            lo = mid+1
        else:
            hi = mid
    
    lis[hi] = k
    return lis
    
n = int(input())

nList = []
for i in range(n):
    nList.append(list(map(int,input().split())))
nList.sort()

LIS = [nList[0][1]]
answer = 1

for i in range(1,n):
    if LIS[-1] < nList[i][1]:
        LIS.append(nList[i][1])
        answer += 1
    
    else:
        LIS = BS(LIS, nList[i][1])

print(n-answer)
import sys
N, M = map(int, sys.stdin.readline().split())
nList = list(map(int, sys.stdin.readline().split()))

maxLen = max(nList)

def solution(arr, target, start, end):
    while end >= start:
        mid = (start+end)//2
        cnt = 0

        for i in arr:
            cnt += 0 if i<mid else i-mid
            
        if cnt >= target:
            start = mid+1
        else:
            end = mid-1

    return end

print(solution(nList, M, 1, maxLen))
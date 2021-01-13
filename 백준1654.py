import sys

N, K = map(int, sys.stdin.readline().split())
nList = list(int(sys.stdin.readline()) for _ in range(N))

totalN = sum(nList)
maxLen = totalN//K

def solution(arr, target, start, end):
    while end >= start:
        mid = (start+end)//2
        cnt = 0

        for i in arr:
            cnt += i//mid
            if cnt > target:
                break

        if cnt >= target:
            start = mid+1
        else:
            end = mid-1

    return end


print(solution(nList, K, 1, maxLen))
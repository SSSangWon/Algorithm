import sys
r = sys.stdin.readline

N, k = int(r()), int(r())

start = 1
end = k
answer = 0

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for i in range(1, N+1):
        cnt += min(mid//i, N)
    
    if cnt < k:
        start = mid+1
    else:
        answer = mid
        end = mid-1

print(answer)
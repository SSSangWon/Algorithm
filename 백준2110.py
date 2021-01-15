import sys
r = sys.stdin.readline

N, C = map(int, r().split())
nList = list(int(r()) for _ in range(N))
nList.sort()

start = 1
end = nList[-1] - nList[0]
answer = 0

def check():
    cnt = 1
    t = nList[0]

    for i in range(1, N):
        if (nList[i] - t) >= mid:
            cnt += 1
            t = nList[i]

    if cnt >= C:
        return True
    else:
        return False


while start <= end:
    mid = (start+end)//2
    if check():
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
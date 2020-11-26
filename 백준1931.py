n = int(input())

nList = [list(map(int,input().split())) for i in range(n)]
nList.sort(key = lambda x : (x[1], x[0]))

cnt = 1
startTime = nList[0][0]
endTime = nList[0][1]

print(nList)

for i in nList[1:]:
    startTime = i[0]
    if startTime >= endTime:
        endTime = i[1]
        cnt += 1
        print(endTime)

print(cnt)
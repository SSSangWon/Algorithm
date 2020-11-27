n = int(input())
nList = list(map(int,input().split()))

nList.sort()

for i in range(1,n):
    nList[i] += nList[i-1]

print(sum(nList))

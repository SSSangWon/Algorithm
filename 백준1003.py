n = int(input())
maxNum = 0
nList = []
for i in range(n):
    nList.append(int(input()))
    if maxNum < nList[i]:
        maxNum = nList[i]
    

zeroList = list(0 for i in range(maxNum+1))
oneList = list(0 for i in range(maxNum+1))

zeroList[0]=1
oneList[1]=1

for i in range(2,maxNum+1):
    zeroList[i] = zeroList[i-1] + zeroList[i-2]
    oneList[i] = oneList[i-1] + oneList[i-2]


for i in nList:
    print(zeroList[i], oneList[i])

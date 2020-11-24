n = int(input())
nList = []

for i in range(n):
    nList.append(int(input()))

answerList = [0 for i in range(n+1)]
nList.insert(0,0)

if n == 0:
    print(nList[0])

if n == 1:
    print(nList[1])

elif n == 2:
    print(nList[1] + nList[2])

elif n > 2:
    answerList[1] = nList[1]
    answerList[2] = nList[1] + nList[2]

    for i in range(3,n+1):
        answerList[i] = max(nList[i-1]+answerList[i-3], answerList[i-2] ) + nList[i]
    
    print(answerList[n])
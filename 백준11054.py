n = int(input())
nList = list(map(int,input().split()))

answer = 0

answerList = list(1 for i in range(n))
re_answerList = list(1 for i in range(n))

for i in range(n):
    for j in range(i, n):
        if answerList[i] == answerList[j] and nList[i] < nList[j]:
            answerList[j] += 1

for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        if re_answerList[i] == re_answerList[j] and nList[i] < nList[j]:
            re_answerList[j] += 1
            
for i in range(n):
    answer = max(answer, answerList[i]+re_answerList[i])

print(answer-1)
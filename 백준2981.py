import math

def DIV(n1):
    divList=[n1]
    for i in range(2,int(n1**0.5)+1):
        if n1%i == 0:
            divList.append(i)
            if n1//i != i:
                divList.append(n1//i)
    divList.sort()
    return divList

n = int(input())
nList = [int(input()) for i in range(n)]

answer = nList[1]-nList[0]

for i in range(2,n):
    answer = math.gcd(answer, nList[i]-nList[i-1])

print(*DIV(answer))
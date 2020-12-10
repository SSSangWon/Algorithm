from functools import reduce

n = int(input())

for i in range(n):
    n1 = int(input())
    mul = 1
    pDic = {}
    for j in range(n1):
        p1, p2= map(str,input().split())

        if p2 in pDic:
            pDic[p2]+=1

        else:
            pDic[p2] = 1
    
    for i in pDic.values():
        mul *= (i+1)
    
    print(mul-1)

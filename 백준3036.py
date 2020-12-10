import math

n = int(input())

nList = list(map(int,input().split()))

for i in range(1, n):
    gcd = math.gcd(nList[0], nList[i])
    print('%d/%d'% (nList[0]//gcd, nList[i]//gcd))
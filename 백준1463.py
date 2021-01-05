import sys

n = int(sys.stdin.readline())

nList = list(1 for i in range(n+1))
nList[1] = 0

for i in range(4,n+1):
    if i%6 == 0:
        nList[i] = min(nList[i//2]+1, nList[i//3]+1)
    elif i%3 == 0:
        nList[i] = min(nList[i//3]+1, nList[i-1]+1)
    elif i%2 == 0:
        nList[i] = min(nList[i//2]+1, nList[i-1]+1)
    else:
        nList[i] = nList[i-1]+1
    

print(nList[n]) 

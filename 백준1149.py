n = int(input())
nList = [list(map(int,input().split())) for i in range(n)]

RED, GREEN, BLUE = nList[0][0], nList[0][1], nList[0][2]

for i in range(1,n):
    tR, tG, tB = RED, GREEN, BLUE
        
    RED = min(tG, tB) + nList[i][0]
    GREEN = min(tR, tB) + nList[i][1]
    BLUE = min(tR, tG) + nList[i][2]
    
print(min([RED, GREEN, BLUE]))
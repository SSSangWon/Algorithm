import sys

n = int(sys.stdin.readline())
nList = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))

cntMo, cntZ, cntO = 0, 0, 0

def solution(x, y, N):
    global cntMo, cntZ, cntO
    check = nList[x][y]
    sw = True

    for i in range(x, x+N):
        for j in range(y, y+N):
            if nList[i][j] != check:
                sw = False
                break

    if sw:
        if check == -1:
            cntMo += 1
        elif check == 0:
            cntZ += 1
        elif check == 1:
            cntO += 1

    else:
        solution(x, y, N//3)
        solution(x+N//3, y, N//3) 
        solution(x+N//3*2, y, N//3)
        solution(x, y+N//3, N//3)
        solution(x+N//3, y+N//3, N//3) 
        solution(x+N//3*2, y+N//3, N//3)
        solution(x, y+N//3*2, N//3)
        solution(x+N//3, y+N//3*2, N//3) 
        solution(x+N//3*2, y+N//3*2, N//3)

    return

solution(0, 0, n)
print(cntMo)
print(cntZ)
print(cntO)
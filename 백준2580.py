import sys

sudoku = list(list(map(int, input().split())) for i in range(9))

zeros=[]
cntZero=0

# 값이 없는 위치를 저장
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zeros.append([i,j])
            cntZero+=1


# 가로 검사 
def checkX(cx, v):
    if v in sudoku[cx]:
        return False
    return True

# 세로 검사
def checkY(cy, v):
    for i in range(9):
        if v == sudoku[i][cy]:
            return False
    return True

# 33 검사
def check33(cx, cy, v):

    for i in range(3):
        for j in range(3):
            if v == sudoku[cx//3*3+i][cy//3*3+j]:
                return False
    return True

def solution(n):

    if n == cntZero:
        for i in sudoku:
            print(*i)
        sys.exit()
    
    else:
        x = zeros[n][0]
        y = zeros[n][1]

        for i in range(1, 10):

            if checkX(x, i)  and checkY(y, i) and check33(x, y, i):
                sudoku[x][y] = i
                solution(n+1)
                sudoku[x][y] = 0

solution(0)

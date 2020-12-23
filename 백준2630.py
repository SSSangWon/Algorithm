import sys

n = int(sys.stdin.readline())
nList = list(list(map(int,sys.stdin.readline().rsplit())) for i in range(n))

b, w = 0, 0

def solution(x, y, N):
    global b, w
    check = nList[x][y]
    sw = True

    for i in range(x, x+N):
        for j in range(y, y+N):
            if nList[i][j] != check:
                sw = False
                break

    if sw:
        if check == 0:
            w += 1
        elif check == 1:
            b += 1
    else:
        solution(x, y, N//2)
        solution(x + N//2, y, N//2)
        solution(x, y + N//2, N//2)
        solution(x + N//2, y + N//2, N//2)

    return

solution(0, 0, n)
print(w)
print(b)
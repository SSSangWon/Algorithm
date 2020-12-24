import sys

n = int(sys.stdin.readline())
nList = list(sys.stdin.readline() for i in range(n))
answer = ''
def solution(x, y, N):
    global answer

    check = nList[y][x]
    sw = True
    for i in nList[y:y+N]:
        for j in i[x:x+N]:
            if check != j:
                sw = False
                break

    if N > 1:
        if sw:
            answer+=check
        
        else:
            answer += '('
            solution(x, y, N//2)
            solution(x + N//2, y, N//2)
            solution(x, y + N//2, N//2)
            solution(x + N//2, y + N//2, N//2)

            answer += ')'
    else:
        answer+=nList[y][x]

    return

solution(0, 0, n)
print(answer)